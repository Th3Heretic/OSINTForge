import requests
from bs4 import BeautifulSoup

def run(target):
    print(f"Scraping metadata for: {target}")

    try:
        # Fetch the website content
        response = requests.get(target, timeout=5)
        response.raise_for_status()  # Raise HTTP errors

        # Parse the website content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract metadata
        print("\nWebsite Metadata:\n")
        title = soup.title.string if soup.title else "No title found"
        print(f"Title: {title}")

        description = soup.find("meta", attrs={"name": "description"})
        description_content = description["content"] if description else "No description found"
        print(f"Description: {description_content}")

        keywords = soup.find("meta", attrs={"name": "keywords"})
        keywords_content = keywords["content"] if keywords else "No keywords found"
        print(f"Keywords: {keywords_content}")

        # Extract HTTP headers
        print("\nHTTP Headers:\n")
        for header, value in response.headers.items():
            print(f"{header}: {value}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching website: {e}")
    except Exception as e:
        print(f"Error during metadata scraping: {e}")