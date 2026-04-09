"""
subdomain_enum.py

Performs wordlist-based subdomain enumeration using a local wordlist
stored in OSINTForge/data/subdomains.txt.

Designed for use in authorized, controlled environments only.
"""

from __future__ import annotations

from pathlib import Path
import socket
from concurrent.futures import ThreadPoolExecutor, as_completed
import random


def _project_root() -> Path:
    """
    Resolve the project root from this module location.
    Assumes this file lives in OSINTForge/modules/.
    """
    return Path(__file__).resolve().parent.parent


def load_wordlist() -> list[str]:
    """
    Load and clean the local subdomain wordlist.
    """
    path = _project_root() / "data" / "subdomains.txt"

    if not path.is_file():
        return []

    with open(path, "r", encoding="utf-8", errors="replace") as file_handle:
        raw = file_handle.read()

    cleaned = raw.replace('"', "").replace(",", "").split()
    return sorted(set(word.strip() for word in cleaned if word.strip()))


def _resolve(hostname: str) -> dict | None:
    """
    Resolve a hostname to its associated IP addresses.
    """
    try:
        canonical, aliases, ips = socket.gethostbyname_ex(hostname)
        return {
            "host": hostname,
            "canonical": canonical,
            "aliases": aliases,
            "ips": ips
        }
    except socket.gaierror:
        return None
    except Exception as exc:
        return {"host": hostname, "error": str(exc)}


def detect_wildcard(domain: str, trials: int = 3) -> tuple[bool, tuple | None]:
    """
    Detect wildcard DNS by resolving random nonsense subdomains.
    If they consistently resolve to the same IPs, wildcard DNS is likely present.
    """
    results = []

    for _ in range(trials):
        randlabel = f"{random.getrandbits(64):x}"
        hostname = f"{randlabel}.{domain}"
        result = _resolve(hostname)

        if result and "ips" in result and result["ips"]:
            results.append(tuple(sorted(result.get("ips", []))))

    if len(results) >= 2 and all(entry == results[0] for entry in results):
        return True, results[0]

    return False, None


def run(domain: str, threads: int = 50) -> None:
    """
    Run subdomain enumeration against a domain.
    """
    print(f" - Running subdomain enumeration for: {domain}")

    wordlist = load_wordlist()
    if not wordlist:
        print(" - Wordlist appears empty or was not found (check OSINTForge/data/subdomains.txt).")
        return

    wildcard, ips = detect_wildcard(domain)
    if wildcard:
        print(f" - Wildcard DNS appears to be present. Example IPs: {', '.join(ips)}")
        print(" - Aborting brute-force enumeration to avoid false positives.")
        return

    found = []

    with ThreadPoolExecutor(max_workers=threads) as executor:
        future_map = {}

        for label in wordlist:
            subdomain = f"{label}.{domain}"
            future = executor.submit(_resolve, subdomain)
            future_map[future] = subdomain

        for future in as_completed(future_map):
            result = future.result()
            subdomain = future_map[future]

            if result is None:
                continue

            if "error" in result:
                continue

            resolved_ips = result.get("ips", [])
            if resolved_ips:
                print(f" - Found: {subdomain} -> {', '.join(resolved_ips)}")
                found.append({
                    "subdomain": subdomain,
                    "ips": resolved_ips
                })

    if not found:
        print(" - No subdomains discovered from the provided wordlist.")
    else:
        print(f" - Enumeration complete. {len(found)} subdomains discovered.")


if __name__ == "__main__":
    run("example.com")