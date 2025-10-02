import requests
from bs4 import BeautifulSoup

def run(target):
    output = []
    output.append(f"Scraping metadata for: {target}")

    try:
        # Fetch the website content
        response = requests.get(target, timeout=5)
        response.raise_for_status()  # Raise HTTP errors

        # Parse the website content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract metadata
        output.append("\nWebsite Metadata:\n")
        title = soup.title.string if soup.title else "No title found"
        output.append(f"Title: {title}")

        description = soup.find("meta", attrs={"name": "description"})
        description_content = description["content"] if description else "No description found"
        output.append(f"Description: {description_content}")

        keywords = soup.find("meta", attrs={"name": "keywords"})
        keywords_content = keywords["content"] if keywords else "No keywords found"
        output.append(f"Keywords: {keywords_content}")

        # Extract HTTP headers
        output.append("\nHTTP Headers:\n")
        headers_formatted = "\n".join([f"{header}: {value}" for header, value in response.headers.items()])
        output.append(headers_formatted)

    except requests.exceptions.RequestException as e:
        output.append(f"[ERROR] Request failed: {e}")
    except Exception as e:
        output.append(f"[ERROR] Metadata scraping failed: {e}")

    return "\n".join(output)