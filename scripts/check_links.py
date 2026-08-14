#!/usr/bin/env python3
"""Check catalog links without modifying the registry."""

from __future__ import annotations

import argparse
import json
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "papers.json"
USER_AGENT = "Awesome-Exploration-Link-Check/1.0"
RANGE_HEADERS = {"User-Agent": USER_AGENT, "Range": "bytes=0-0"}


@dataclass(frozen=True)
class LinkResult:
    """A link is reachable, unverifiable, or definitively failed."""

    state: str
    detail: int | str


def request_url(url: str, method: str, headers: dict[str, str], timeout: float) -> LinkResult:
    request = urllib.request.Request(url, method=method, headers=headers)
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return LinkResult("reachable", response.status)
    except urllib.error.HTTPError as error:
        if error.code in {403, 429}:
            return LinkResult("unverifiable", error.code)
        return LinkResult("failed", error.code)
    except Exception as error:  # noqa: BLE001 - report network failures verbatim
        return LinkResult("failed", type(error).__name__)


def check(url: str, timeout: float) -> tuple[str, LinkResult]:
    """Probe with HEAD, then use a one-byte GET only when HEAD is unsupported."""
    result = request_url(url, "HEAD", {"User-Agent": USER_AGENT}, timeout)
    if result.state == "failed" and result.detail == 405:
        result = request_url(url, "GET", RANGE_HEADERS, timeout)
    return url, result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=12)
    parser.add_argument("--timeout", type=float, default=15)
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Treat access-limited links as a failing verification result.",
    )
    args = parser.parse_args()

    catalog = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    urls = sorted(
        {paper["url"] for paper in catalog["papers"]}
        | {paper["url"] for paper in catalog["classics"]}
        | {
            paper["publication"]["official_url"]
            for paper in catalog["papers"]
            if (paper.get("publication") or {}).get("evidence") == "official"
        }
    )
    results: dict[str, LinkResult] = {}
    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = {executor.submit(check, url, args.timeout): url for url in urls}
        for future in as_completed(futures):
            url, result = future.result()
            results[url] = result

    reachable = {url: result for url, result in results.items() if result.state == "reachable"}
    unverifiable = {url: result for url, result in results.items() if result.state == "unverifiable"}
    failures = {url: result for url, result in results.items() if result.state == "failed"}
    print(
        f"Checked {len(urls)} links: {len(reachable)} reachable, "
        f"{len(unverifiable)} unverifiable, {len(failures)} failed"
    )
    for label, entries in (("Unverifiable", unverifiable), ("Failed", failures)):
        for url, result in entries.items():
            print(f"- {label} ({result.detail}): {url}")
    return 1 if failures or (args.strict and unverifiable) else 0


if __name__ == "__main__":
    raise SystemExit(main())
