#!/usr/bin/env python3
"""Check catalog links without modifying the registry."""

from __future__ import annotations

import argparse
import json
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "papers.json"
USER_AGENT = "Awesome-Exploration-Link-Check/1.0"


def check(url: str, timeout: float) -> tuple[str, int | str]:
    request = urllib.request.Request(url, method="HEAD", headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return url, response.status
    except urllib.error.HTTPError as error:
        # Some publication sites reject HEAD but serve the page normally.
        if error.code in {403, 405, 429}:
            return url, error.code
        return url, error.code
    except Exception as error:  # noqa: BLE001 - report network failures verbatim
        return url, type(error).__name__


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=12)
    parser.add_argument("--timeout", type=float, default=15)
    args = parser.parse_args()

    catalog = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    urls = sorted(
        {paper["url"] for paper in catalog["papers"]}
        | {paper["url"] for paper in catalog["classics"]}
    )
    results: dict[str, int | str] = {}
    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = {executor.submit(check, url, args.timeout): url for url in urls}
        for future in as_completed(futures):
            url, status = future.result()
            results[url] = status

    failures = {
        url: status
        for url, status in results.items()
        if not (isinstance(status, int) and (200 <= status < 400 or status in {403, 405, 429}))
    }
    blocked = sum(status in {403, 405, 429} for status in results.values() if isinstance(status, int))
    print(f"Checked {len(urls)} links: {len(urls) - len(failures)} reachable, {blocked} access-limited, {len(failures)} failed")
    for url, status in failures.items():
        print(f"- {status}: {url}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
