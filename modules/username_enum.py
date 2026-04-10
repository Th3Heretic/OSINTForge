import requests
from bs4 import BeautifulSoup
import time
from concurrent.futures import ThreadPoolExecutor, as_completed


SITES = {
    "Twitter": "https://twitter.com/{}",
    "Instagram": "https://www.instagram.com/{}/",
    "YouTube": "https://www.youtube.com/{}",
    "Threads": "https://www.threads.net/@{}",
    "Reddit": "https://www.reddit.com/user/{}/",
    "Pinterest": "https://www.pinterest.com/{}/",
    "TikTok": "https://www.tiktok.com/@{}",
    "LinkedIn": "https://www.linkedin.com/in/{}/",
    "Tumblr": "https://{}.tumblr.com/",
    "HackerRank": "https://www.hackerrank.com/{}",
    "GitHub": "https://github.com/{}",
    "GitLab": "https://gitlab.com/{}",
    "Dev.to": "https://dev.to/{}",
    "Stack Overflow": "https://stackoverflow.com/users/{}/",
    "HackTheBox": "https://www.hackthebox.com/home/users/profile/{}",
    "Steam": "https://steamcommunity.com/id/{}/",
    "Twitch": "https://www.twitch.tv/{}",
    "Xbox Gamertag": "https://www.xboxgamertag.com/search/{}",
    "Epic Games": "https://www.epicgames.com/id/{}",
    "PlayStation Network": "https://my.playstation.com/profile/{}",
    "Patreon": "https://www.patreon.com/{}",
    "Fiverr": "https://www.fiverr.com/{}",
}


def _clean_text(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    return soup.get_text(" ", strip=True).lower()


def _classify_site_result(site, url, username, headers):
    target_url = url.format(username)
    username_lower = username.lower()

    try:
        response = requests.get(
            target_url,
            headers=headers,
            timeout=5,
            allow_redirects=True
        )

        if response.status_code == 429:
            time.sleep(5)
            response = requests.get(
                target_url,
                headers=headers,
                timeout=5,
                allow_redirects=True
            )

        final_url = response.url.lower()
        page_text = _clean_text(response.text)

        if response.status_code == 404:
            return {
                "site": site,
                "url": target_url,
                "status": "not_found",
                "detail": "404 Not Found"
            }

        if response.status_code == 200:
            username_in_text = username_lower in page_text
            username_in_url = username_lower in final_url

            if username_in_text or username_in_url:
                return {
                    "site": site,
                    "url": target_url,
                    "status": "confirmed",
                    "detail": f"200 OK (matched content{' and URL' if username_in_url and username_in_text else ''})"
                }

            return {
                "site": site,
                "url": target_url,
                "status": "possible",
                "detail": "200 OK but weak confirmation"
            }

        if response.status_code in {401, 403, 999}:
            return {
                "site": site,
                "url": target_url,
                "status": "possible",
                "detail": f"Access restricted / anti-bot response ({response.status_code})"
            }

        return {
            "site": site,
            "url": target_url,
            "status": "error",
            "detail": f"Returned status code {response.status_code}"
        }

    except requests.exceptions.SSLError:
        return {
            "site": site,
            "url": target_url,
            "status": "error",
            "detail": "SSL error"
        }

    except requests.exceptions.RequestException as exc:
        return {
            "site": site,
            "url": target_url,
            "status": "error",
            "detail": str(exc)
        }


def check_username(username):
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/123.0.0.0 Safari/537.36"
        )
    }

    results = []

    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = {
            executor.submit(_classify_site_result, site, url, username, headers): site
            for site, url in SITES.items()
        }

        for future in as_completed(futures):
            results.append(future.result())

    return results


def run(target):
    print(f"Checking username: {target}")
    results = check_username(target)

    confirmed = [r for r in results if r["status"] == "confirmed"]
    possible = [r for r in results if r["status"] == "possible"]
    errors = [r for r in results if r["status"] == "error"]
    not_found = [r for r in results if r["status"] == "not_found"]

    print("\nUsername Enumeration Results:")

    if confirmed:
        print("\n[Confirmed Matches]")
        for result in sorted(confirmed, key=lambda x: x["site"]):
            print(f"[+] {result['site']}: {result['url']}")

    if possible:
        print("\n[Possible Matches / Manual Review]")
        for result in sorted(possible, key=lambda x: x["site"]):
            print(f"[?] {result['site']}: {result['url']} ({result['detail']})")

    if errors:
        print("\n[Errors / Blocked Sites]")
        for result in sorted(errors, key=lambda x: x["site"]):
            print(f"[!] {result['site']}: {result['detail']}")

    if not confirmed and not possible:
        print("[-] No likely username matches found.")

    print(
        f"\nSummary: {len(confirmed)} confirmed, "
        f"{len(possible)} possible, "
        f"{len(errors)} errors/blocked, "
        f"{len(not_found)} not found, "
        f"{len(results)} sites checked."
    )

    return results