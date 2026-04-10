"""
directory_scanner.py

Scans a target URL for common directories and reports interesting HTTP responses.
Intended for ethical use in controlled environments only.
"""

from __future__ import annotations

from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests


def _project_root() -> Path:
    """
    Resolve the project root from this module location.
    Assumes this file lives in OSINTForge/modules/.
    """
    return Path(__file__).resolve().parent.parent


def _normalise_target(target: str) -> str:
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


def run(target: str) -> None:
    """
    Scan a target URL for interesting directory responses.
    """
    print(f" - Scanning directories on: {target}")

    wordlist = load_wordlist()
    if not wordlist:
        print(" - Wordlist appears empty or was not found (check OSINTForge/data/directories.txt).")
        return

    try:
        base_url = _normalise_target(target)
    except Exception as exc:
        print(f" - Error normalising target: {exc}")
        return

    interesting_statuses = {200, 301, 302, 307, 308, 401, 403}
    found = []

    session = requests.Session()
    session.headers.update({
        "User-Agent": "OSINTForge/1.0"
    })

    for directory in wordlist:
        url = urljoin(base_url, f"{directory}/")

        try:
            response = session.get(
                url,
                timeout=5,
                allow_redirects=False
            )

            if response.status_code in interesting_statuses:
                print(f" - Found: {url} -> {response.status_code} {response.reason}")
                found.append({
                    "url": url,
                    "status_code": response.status_code,
                    "reason": response.reason
                })

        except requests.exceptions.ConnectionError:
            print(f" - Error: Could not connect to target '{base_url}'.")
            return
        except requests.exceptions.RequestException as exc:
            # Ignore noisy per-path failures but keep going
            continue

    if not found:
        print(" - No interesting directories found.")
    else:
        print(f" - Scan complete. {len(found)} interesting directory/directories discovered.")