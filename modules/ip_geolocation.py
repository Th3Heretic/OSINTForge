import requests

def run(target):
    print(f"Performing IP Geolocation for: {target}")

    try:
        # Validate the IP format
        if not is_valid_ip(target):
            print(f"Error: Invalid IP address - {target}")
            return

        # Query the ip-api service
        url = f"http://ip-api.com/json/{target}"
        response = requests.get(url)
        data = response.json()

        # Check the response status
        if data['status'] == 'fail':
            print(f"Error: {data['message']}")
            return

        # Display geolocation data
        print("Geolocation Results:\n")
        print(f"IP Address: {data['query']}")
        print(f"Country: {data['country']}")
        print(f"Region: {data['regionName']}")
        print(f"City: {data['city']}")
        print(f"ZIP: {data['zip']}")
        print(f"ISP: {data['isp']}")
        print(f"Latitude: {data['lat']}, Longitude: {data['lon']}")
    except Exception as e:
        print(f"Error during IP Geolocation: {e}")


def is_valid_ip(ip):
    # Basic validation for IPv4 format
    parts = ip.split(".")
    if len(parts) != 4:
        return False
    try:
        return all(0 <= int(part) <= 255 for part in parts)
    except ValueError:
        return False