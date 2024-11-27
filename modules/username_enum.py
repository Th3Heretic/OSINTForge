import requests
from bs4 import BeautifulSoup
import time
from concurrent.futures import ThreadPoolExecutor

# List of websites to check (can be expanded)
SITES = {
    # Social Media
    "Twitter": "https://twitter.com/{}",
    "Instagram": "https://www.instagram.com/{}/",
    "YouTube": "https://www.youtube.com/{}",
    "Threads": "https://www.threads.net/@{}",
    "Reddit": "https://www.reddit.com/user/{}/",
    "Pinterest": "https://www.pinterest.com/{}/",
    "TikTok": "https://www.tiktok.com/@{}",
    "LinkedIn": "https://www.linkedin.com/in/{}/",
    "Tumblr": "https://{}.tumblr.com/",

    # Developer Platforms
    "HackerRank": "https://www.hackerrank.com/{}",
    "GitHub": "https://github.com/{}",
    "GitLab": "https://gitlab.com/{}",
    "Dev.to": "https://dev.to/{}",
    "Stack Overflow": "https://stackoverflow.com/users/{}/",
    "HackTheBox": "https://www.hackthebox.com/home/users/profile/{}",

    # Gaming Platforms
    "Steam": "https://steamcommunity.com/id/{}/",
    "Twitch": "https://www.twitch.tv/{}",
    "Xbox Gamertag": "https://www.xboxgamertag.com/search/{}",
    "Epic Games": "https://www.epicgames.com/id/{}",
    "PlayStation Network": "https://my.playstation.com/profile/{}",

    # Other
    "Patreon": "https://www.patreon.com/{}",
    "Fiverr": "https://www.fiverr.com/{}",
}


def check_single_site(site, url, username, headers):
    """Check the presence of a username on a single platform."""
    target_url = url.format(username)
    try:
        response = requests.get(target_url, headers=headers, timeout=5)

        # Handle rate limiting
        if response.status_code == 429:
            time.sleep(10)  # Wait and retry
            response = requests.get(target_url, headers=headers, timeout=5)

        # Handle HTTP 200 OK responses with BeautifulSoup validation
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            if username.lower() in soup.text.lower():
                return f"[+] Found on {site}: {target_url}"
            else:
                return f"[-] Not found on {site} (False positive filtered)"

        # Handle HTTP 404 Not Found
        elif response.status_code == 404:
            return f"[-] Not found on {site}"

        # Handle other HTTP responses
        else:
            return f"[?] {site} returned status code {response.status_code}"

    except requests.exceptions.SSLError:
        return f"[!] SSL Error checking {site}: Skipping due to certificate issues."

    except requests.exceptions.RequestException as e:
        return f"[!] Error checking {site}: {str(e)}"


def check_username(username):
    """Check the presence of a username on multiple platforms."""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    results = []
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = {executor.submit(check_single_site, site, url, username, headers): site for site, url in SITES.items()}
        for future in futures:
            results.append(future.result())
    return results


def run(target):
    """Run the Username Enumeration module."""
    print(f"Checking username: {target}")
    results = check_username(target)
    print("\nUsername Enumeration Results:")
    for result in results:
        print(result)