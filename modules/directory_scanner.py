"""
directory_scanner.py

Scans a target URL for common directories and reports interesting HTTP responses.
Intended for ethical use in controlled environments only.
"""

from __future__ import annotations

from pathlib import Path
from urllib.parse import urljoin, urlparse
from concurrent.futures import ThreadPoolExecutor, as_completed

import requests


def _project_root() -> Path:
    """
    Resolve the project root from this module location.
    Assumes this file lives in OSINTForge/modules/.
    """
    return Path(__file__).resolve().parent.parent


def normalise_target(target: str) -> str:
    """
    Normalise user input into a usable base URL.
    Accepts bare domains like 'example.com' and converts them to HTTPS.
    """
    target = target.strip()

    if not target.startswith(("http://", "https://")):
        target = f"https://{target}"

    parsed = urlparse(target)
    normalised = f"{parsed.scheme}://{parsed.netloc}"

    if not normalised.endswith("/"):
        normalised += "/"

    return normalised


def load_wordlist() -> list[str]:
    """
    Load and clean the local directory wordlist.
    """
    wordlist_path = _project_root() / "data" / "directories.txt"

    if not wordlist_path.is_file():
        return []

    with open(wordlist_path, "r", encoding="utf-8", errors="replace") as file_handle:
        raw = file_handle.read()

    cleaned = raw.replace('"', "").replace(",", "").split()
    return sorted(set(word.strip().strip("/") for word in cleaned if word.strip()))


def _scan_single(session, base_url, directory):
    url = urljoin(base_url, f"{directory}/")

    try:
        response = session.get(
            url,
            timeout=5,
            allow_redirects=False
        )

        if response.status_code in {200, 301, 302, 307, 308, 401, 403, 410, 418}:
            return {
                "url": url,
                "status": response.status_code,
                "reason": response.reason
            }

    except requests.exceptions.RequestException:
        return None

    return None


def run(target: str, threads: int = 30) -> None:
    print(f" - Scanning directories on: {target}")

    wordlist = load_wordlist()
    if not wordlist:
        print(" - Wordlist appears empty or was not found (check OSINTForge/data/directories.txt).")
        return

    try:
        base_url = normalise_target(target)
    except Exception as exc:
        print(f" - Error normalising target: {exc}")
        return

    session = requests.Session()
    session.headers.update({
        "User-Agent": "OSINTForge/1.0"
    })

    found = []

    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = [
            executor.submit(_scan_single, session, base_url, directory)
            for directory in wordlist
        ]

        for future in as_completed(futures):
            result = future.result()
            if result:
                print(f" - Found: {result['url']} -> {result['status']} {result['reason']}")
                found.append(result)

    if not found:
        print(" - No interesting directories found.")
    else:
        print(f" - Scan complete. {len(found)} interesting directories discovered.")