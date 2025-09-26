"""
ssl_certificate.py

Retrieves and parses SSL certificate data from a remote host.
Intended for ethical use in controlled environments only.
"""
import ssl
import socket
from datetime import datetime

def get_ssl_certificate(hostname, port=443):
    """Retrieve SSL certificate details for a given hostname and port."""
    try:
        context = ssl.create_default_context()
        with socket.create_connection((hostname, port)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssl_sock:
                cert = ssl_sock.getpeercert()
                return cert
    except Exception as e:
        return {"error": str(e)}

def parse_certificate(cert):
    """Parse SSL certificate details into a readable format."""
    if "error" in cert:
        return cert

    details = {
        "issuer": dict(x[0] for x in cert.get("issuer", [])),
        "subject": dict(x[0] for x in cert.get("subject", [])),
        "valid_from": cert.get("notBefore"),
        "valid_to": cert.get("notAfter"),
        "version": cert.get("version", "N/A"),
        "serial_number": cert.get("serialNumber", "N/A"),
        "fingerprint_sha256": cert.get("sha256Fingerprint", "N/A"),
        "fingerprint_md5": cert.get("md5Fingerprint", "N/A"),
    }

    # Convert valid_from and valid_to to readable datetime format
    try:
        details["valid_from"] = datetime.strptime(details["valid_from"], "%b %d %H:%M:%S %Y %Z").strftime("%Y-%m-%d %H:%M:%S")
        details["valid_to"] = datetime.strptime(details["valid_to"], "%b %d %H:%M:%S %Y %Z").strftime("%Y-%m-%d %H:%M:%S")
    except Exception:
        pass

    return details

def format_nested_dict(data):
    """Format nested dictionaries for clean output."""
    return "\n    ".join([f"{k}: {v}" for k, v in data.items()])

def run(target):
    """Retrieve and display SSL certificate details."""
    print(f"\n - Retrieving SSL certificate details for: {target}")
    cert = get_ssl_certificate(target)
    details = parse_certificate(cert)

    if "error" in details:
        print(f" - Error: {details['error']}")
    else:
        print("\n - SSL Certificate Details:")
        for key, value in details.items():
            if isinstance(value, dict):  # Prettify nested dictionaries
                print(f" - {key.replace('_', ' ').capitalize()}:\n    {format_nested_dict(value)}")
            else:
                print(f" - {key.replace('_', ' ').capitalize()}: {value}")