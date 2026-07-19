#!/usr/bin/env python3
"""Audit structural quality of the Awesome Exploration Markdown catalog.

This is intentionally network-free. It detects local duplication, identifier
collisions, and drift between the compact and detailed views. Use external
metadata verification separately to prove that a title matches its URL.
"""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
import unicodedata
from collections import defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable


# Catalog entries carry a mechanism badge. Requiring it avoids treating bold
# bullets in prose sections (for example, open research questions) as papers.
ENTRY_RE = re.compile(r'^\s*-\s+\*\*"?(.+?)"?\*\*.*shields\.io')
SECTION_RE = re.compile(r'^##\s+([1-8]\..+)$')
HEADING_RE = re.compile(r'^#{1,6}\s+')
ARXIV_RE = re.compile(r'https?://(?:www\.)?arxiv\.org/abs/(\d{4}\.\d{4,5})(?:v\d+)?', re.I)
DOI_RE = re.compile(r'https?://(?:dx\.)?doi\.org/([^\s)\]]+)', re.I)


@dataclass(frozen=True)
class Entry:
    title: str
    normalized_title: str
    line: int
    section: str
    identifiers: tuple[str, ...]


def normalize_title(value: str) -> str:
    value = html.unescape(unicodedata.normalize('NFKC', value))
    value = value.strip().strip('"“”')
    value = value.replace('\u00a0', ' ')
    return re.sub(r'\s+', ' ', value).casefold()


def extract_identifiers(block: str) -> tuple[str, ...]:
    identifiers = {f'arxiv:{match}' for match in ARXIV_RE.findall(block)}
    identifiers.update(f'doi:{match.rstrip(".").casefold()}' for match in DOI_RE.findall(block))
    return tuple(sorted(identifiers))


def parse_catalog(path: Path) -> list[Entry]:
    lines = path.read_text(encoding='utf-8-sig').splitlines()
    entries: list[Entry] = []
    section = '(before numbered sections)'

    for index, line in enumerate(lines):
        section_match = SECTION_RE.match(line)
        if section_match:
            section = section_match.group(1)

        entry_match = ENTRY_RE.match(line)
        if not entry_match:
            continue

        end = index + 1
        while end < len(lines):
            if ENTRY_RE.match(lines[end]) or HEADING_RE.match(lines[end]):
                break
            end += 1

        title = entry_match.group(1).strip().strip('"“”')
        entries.append(
            Entry(
                title=title,
                normalized_title=normalize_title(title),
                line=index + 1,
                section=section,
                identifiers=extract_identifiers('\n'.join(lines[index:end])),
            )
        )

    return entries


def grouped_duplicates(entries: Iterable[Entry]) -> dict[str, list[Entry]]:
    grouped: dict[str, list[Entry]] = defaultdict(list)
    for entry in entries:
        grouped[entry.normalized_title].append(entry)
    return {key: value for key, value in grouped.items() if len(value) > 1}


def identifier_collisions(entries: Iterable[Entry]) -> dict[str, list[Entry]]:
    grouped: dict[str, list[Entry]] = defaultdict(list)
    for entry in entries:
        for identifier in entry.identifiers:
            grouped[identifier].append(entry)
    return {
        identifier: values
        for identifier, values in grouped.items()
        if len({value.normalized_title for value in values}) > 1
    }


def catalog_summary(entries: list[Entry]) -> dict[str, int]:
    duplicates = grouped_duplicates(entries)
    identifiers = {identifier for entry in entries for identifier in entry.identifiers}
    return {
        'entries': len(entries),
        'unique_titles': len({entry.normalized_title for entry in entries}),
        'duplicate_title_groups': len(duplicates),
        'duplicate_occurrences': sum(len(values) - 1 for values in duplicates.values()),
        'unique_primary_identifiers': len(identifiers),
        'identifier_collision_groups': len(identifier_collisions(entries)),
    }


def make_report(root: Path) -> dict[str, object]:
    compact_path = root / 'README.md'
    detailed_path = root / 'README_DETAILED.md'
    missing = [str(path.relative_to(root)) for path in (compact_path, detailed_path) if not path.exists()]
    if missing:
        return {'root': str(root), 'missing_files': missing}

    compact = parse_catalog(compact_path)
    detailed = parse_catalog(detailed_path)
    compact_titles = {entry.normalized_title for entry in compact}
    detailed_titles = {entry.normalized_title for entry in detailed}

    compact_only = sorted(compact_titles - detailed_titles)
    detailed_only = sorted(detailed_titles - compact_titles)
    nested = root / 'awesome-exploration'

    return {
        'root': str(root),
        'files': {
            'README.md': catalog_summary(compact),
            'README_DETAILED.md': catalog_summary(detailed),
        },
        'view_drift': {
            'compact_only_count': len(compact_only),
            'detailed_only_count': len(detailed_only),
            'compact_only_titles': compact_only,
            'detailed_only_titles': detailed_only,
        },
        'duplicate_titles': {
            'README.md': {
                key: [asdict(entry) for entry in values]
                for key, values in sorted(grouped_duplicates(compact).items())
            },
            'README_DETAILED.md': {
                key: [asdict(entry) for entry in values]
                for key, values in sorted(grouped_duplicates(detailed).items())
            },
        },
        'identifier_collisions': {
            'README.md': {
                key: [asdict(entry) for entry in values]
                for key, values in sorted(identifier_collisions(compact).items())
            },
            'README_DETAILED.md': {
                key: [asdict(entry) for entry in values]
                for key, values in sorted(identifier_collisions(detailed).items())
            },
        },
        'nested_catalog_copy_present': nested.is_dir(),
    }


def samples(values: Iterable[str], limit: int) -> str:
    selected = list(values)[:limit]
    if not selected:
        return 'none'
    return '; '.join(selected)


def print_report(report: dict[str, object], verbose: bool, sample_limit: int) -> None:
    if report.get('missing_files'):
        print(f"Missing files: {', '.join(report['missing_files'])}")
        return

    files = report['files']
    print('Catalog audit')
    for name in ('README.md', 'README_DETAILED.md'):
        summary = files[name]
        print(
            f"- {name}: {summary['entries']} entries, {summary['unique_titles']} unique titles, "
            f"{summary['duplicate_title_groups']} duplicate-title groups "
            f"({summary['duplicate_occurrences']} extra occurrences), "
            f"{summary['identifier_collision_groups']} identifier collisions"
        )

    drift = report['view_drift']
    print(
        f"- View drift: {drift['compact_only_count']} compact-only titles, "
        f"{drift['detailed_only_count']} detailed-only titles"
    )
    print(f"- Nested catalog copy present: {report['nested_catalog_copy_present']}")

    limit = sys.maxsize if verbose else sample_limit
    print(f"- Compact-only examples: {samples(drift['compact_only_titles'], limit)}")
    print(f"- Detailed-only examples: {samples(drift['detailed_only_titles'], limit)}")

    for name in ('README.md', 'README_DETAILED.md'):
        duplicate_titles = report['duplicate_titles'][name]
        collision_ids = report['identifier_collisions'][name]
        print(f"- {name} duplicate-title examples: {samples(duplicate_titles, limit)}")
        print(f"- {name} identifier-collision examples: {samples(collision_ids, limit)}")


def has_strict_failures(report: dict[str, object]) -> bool:
    if report.get('missing_files'):
        return True
    files = report['files']
    drift = report['view_drift']
    return any(
        (
            files['README.md']['duplicate_title_groups'],
            files['README_DETAILED.md']['duplicate_title_groups'],
            files['README.md']['identifier_collision_groups'],
            files['README_DETAILED.md']['identifier_collision_groups'],
            drift['compact_only_count'],
            drift['detailed_only_count'],
            report['nested_catalog_copy_present'],
        )
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--json', action='store_true', help='Emit the full machine-readable report.')
    parser.add_argument('--verbose', action='store_true', help='Print every issue instead of samples.')
    parser.add_argument('--sample-limit', type=int, default=5)
    parser.add_argument(
        '--strict',
        action='store_true',
        help='Exit non-zero on duplicates, view drift, identifier collisions, or nested copies.',
    )
    args = parser.parse_args()

    report = make_report(args.root.resolve())
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print_report(report, args.verbose, args.sample_limit)

    return 1 if args.strict and has_strict_failures(report) else 0


if __name__ == '__main__':
    raise SystemExit(main())
