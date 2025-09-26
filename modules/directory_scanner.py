"""
directory_scanner.py

Scans a target URL for common directories and logs HTTP responses.
Intended for ethical use in controlled environments only.
"""

import os
import requests
from bs4 import BeautifulSoup

# Used an OS path join to be usable across systems instead of just assuming the OS uses '/' as a directory separator
def load_wordlist():
    wordlist_path = os.path.join("..", "data", "directories.txt")
    with open(wordlist_path, "r") as f:
        raw = f.read()
        cleaned = raw.replace('"', '').replace(',', '').split()
        return sorted(set([word.strip() for word in cleaned if word.strip()]))

wordlist = load_wordlist()

def run(target):
    print(f"Scanning directories on: {target}")

    # Ensure target URL has a trailing slash
    if not target.endswith('/'):
        target += '/'

    try:
        for directory in wordlist:
            url = f"{target}{directory}/"
            try:
                response = requests.get(url, timeout=3)
                print(f"{url} - {response.status_code} {response.reason}")

                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, 'html.parser')
                    body = soup.body.get_text(strip=True) if soup.body else "No body content found"
                    print(f"Response Body Content (first 200 chars):\n\"{body[:200]}...\"\n")

            except requests.exceptions.ConnectionError:
                print(f"Error accessing {url}: Connection error. Is the domain correct?")
                break  # Stop further scanning if the domain is unreachable
            except requests.exceptions.RequestException as e:
                print(f"Error accessing {url}: {e}")

    except Exception as e:
        print(f"Unexpected error during directory scanning: {e}")

if __name__ == "__main__":
    test_target = "http://example.com"
    run(test_target)