# Deprecated: This module has been replaced by `subdomain_enumeration.py`
# using a local wordlist for offline subdomain enumeration.
"""
subdomain_enum.py

Performs wordlist-based subdomain enumeration using a local wordlist (/data/subdomains.txt).
Designed for use in authorized, controlled environments only.
"""

import os
import socket
from concurrent.futures import ThreadPoolExecutor, as_completed
import random
import threading

_wordlist_lock = threading.Lock()

def load_wordlist():
    path = os.path.join("..", "data", "subdomains.txt")
    with open(path, "r") as f:
        raw = f.read()
    cleaned = raw.replace('"', '').replace(',', '').split()
    return sorted(set([w.strip() for w in cleaned if w.strip()]))

def _resolve(hostname):
    try:
        canonical, aliases, ips = socket.gethostbyname_ex(hostname)
        return {"host": hostname, "canonical": canonical, "aliases": aliases, "ips": ips}
    except socket.gaierror:
        return None
    except Exception as e:
        return {"host": hostname, "error": str(e)}

def detect_wildcard(domain, trials=3):
    """
    Quick heuristic to detect wildcard DNS: resolve a few random nonsense subdomains
    and see if they all resolve to the same IP(s).
    """
    results = []
    for _ in range(trials):
        randlabel = f"{random.getrandbits(64):x}"
        name = f"{randlabel}.{domain}"
        res = _resolve(name)
        if res and "ips" in res and res["ips"]:
            results.append(tuple(sorted(res.get("ips", []))))
    if len(results) >= 2 and all(r == results[0] for r in results):
        return True, results[0]
    return False, None

def run(domain, threads=50):
    """
    Run subdomain enumeration against `domain`.
    Prints discovered subdomains and their resolved IPs.
    """
    print(f" - Running subdomain enumeration for: {domain}")

    wordlist = load_wordlist()
    if not wordlist:
        print(" - Wordlist appears empty or was not found (check OSINTForge/data/subdomains.txt).")
        return

    # Wildcard detection — if wildcard DNS present, brute force results will be noisy/false-positive
    wildcard, ips = detect_wildcard(domain)
    if wildcard:
        print(f" - Wildcard DNS appears to be present. Example IPs: {', '.join(ips)}")
        print(" - Aborting brute-force enumeration to avoid false positives. Consider using permutation or passive methods.")
        return

    found = []
    with ThreadPoolExecutor(max_workers=threads) as executor:
        future_map = {}
        for label in wordlist:
            sub = f"{label}.{domain}"
            future = executor.submit(_resolve, sub)
            future_map[future] = sub

        for fut in as_completed(future_map):
            res = fut.result()
            sub = future_map[fut]
            if res is None:
                continue
            if "error" in res:
                continue
            ips = res.get("ips", [])
            if ips:
                print(f" - Found: {sub} -> {', '.join(ips)}")
                found.append({"subdomain": sub, "ips": ips})

    if not found:
        print(" - No subdomains discovered from the provided wordlist.")
    else:
        print(f" - Enumeration complete. {len(found)} subdomains discovered.")

if __name__ == "__main__":
    run("example.com")