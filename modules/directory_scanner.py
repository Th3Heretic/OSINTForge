import requests
from bs4 import BeautifulSoup

def run(target):
    print(f"Scanning directories on: {target}")

    # Wordlist of common directories (can be expanded or loaded from a file)
    wordlist = [
        "admin",
        "login",
        "dashboard",
        "config",
        "backup",
        "uploads",
        "test",
        "old",
        "dev",
        "hidden",
        "test",
        "sd",
    ]

    try:
        # Ensure target URL has a trailing slash
        if not target.endswith('/'):
            target += '/'

        # Scan each directory in the wordlist
        for directory in wordlist:
            url = f"{target}{directory}/"
            try:
                response = requests.get(url, timeout=3)
                print(f"{url} - {response.status_code} {response.reason}")

                # If the response status is 200, extract and print the first 200 characters of the body
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, 'html.parser')
                    body = soup.body.get_text(strip=True) \
                        if soup.body \
                        else "No body content found"
                    print(f"Response Body Content (first 200 chars):\n\" {body[:200]}...\"\n")
            except requests.exceptions.ConnectionError:
                print(f"Error accessing {url}: Connection error. Is the domain correct?")
                break  # Stop further scanning if the domain is unreachable
            except requests.exceptions.RequestException as e:
                print(f"Error accessing {url}: {e}")
    except Exception as e:
        print(f"Error during directory scanning: {e}")