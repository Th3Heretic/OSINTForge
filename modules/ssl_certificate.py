"""
ssl_certificate.py

Retrieves and parses SSL certificate data from a remote host.
Intended for ethical use in controlled environments only.
"""
import ssl
import socket
from datetime import datetime
from urllib.parse import urlparse


def _normalise_target(target: str) -> str:
    target = target.strip()

    if target.startswith(("http://", "https://")):
        parsed = urlparse(target)
        return parsed.netloc

    return target


def get_ssl_certificate(hostname, port=443):
    try:
        context = ssl.create_default_context()
        with socket.create_connection((hostname, port), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssl_sock:
                return ssl_sock.getpeercert()
    except Exception as e:
        return {"error": str(e)}


def parse_certificate(cert):
    if "error" in cert:
        return cert

    details = {
        "issuer": dict(x[0] for x in cert.get("issuer", [])),
        "subject": dict(x[0] for x in cert.get("subject", [])),
        "valid_from": cert.get("notBefore"),
        "valid_to": cert.get("notAfter"),
        "version": cert.get("version", "N/A"),
        "serial_number": cert.get("serialNumber", "N/A"),
    }

    try:
        details["valid_from"] = datetime.strptime(
            details["valid_from"], "%b %d %H:%M:%S %Y %Z"
        ).strftime("%Y-%m-%d %H:%M:%S")

        details["valid_to"] = datetime.strptime(
            details["valid_to"], "%b %d %H:%M:%S %Y %Z"
        ).strftime("%Y-%m-%d %H:%M:%S")

    except Exception:
        pass

    return details


def format_nested_dict(data):
    return "\n    ".join([f"{k}: {v}" for k, v in data.items()])


def run(target):
    target = _normalise_target(target)

    print(f"\n - Retrieving SSL certificate details for: {target}")

    cert = get_ssl_certificate(target)
    details = parse_certificate(cert)

    if "error" in details:
        print(f" - Error: {details['error']}")
        return None

    print("\n - SSL Certificate Details:")

    flat_results = []

    for key, value in details.items():
        display_key = key.replace("_", " ").capitalize()

        if isinstance(value, dict):
            print(f" - {display_key}:\n    {format_nested_dict(value)}")

            for sub_key, sub_value in value.items():
                flat_results.append({
                    "field": f"{display_key}.{sub_key}",
                    "value": sub_value
                })

        else:
            print(f" - {display_key}: {value}")
            flat_results.append({
                "field": display_key,
                "value": value
            })

    return flat_results