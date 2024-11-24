import requests

def run(target):
    print(f"Performing Subdomain Enumeration for: {target}")

    try:
        # Query the SecurityTrails API (free API, requires registration for a key)
        api_key = "CUaGc2Aqwwbv83WscX-PvKRqdwRw1G33"
        headers = {"APIKEY": api_key}
        url = f"https://api.securitytrails.com/v1/domain/{target}/subdomains"

        response = requests.get(url, headers=headers)
        data = response.json()

        if response.status_code == 200:
            subdomains = data.get("subdomains", [])
            print("\nDiscovered Subdomains:\n")
            for subdomain in subdomains:
                print(f"{subdomain}.{target}")
        else:
            print(f"Error: {data.get('message', 'Failed to retrieve subdomains')}")
    except Exception as e:
        print(f"Error during Subdomain Enumeration: {e}")