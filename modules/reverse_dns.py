"""
reverse_dns.py

Performs a reverse DNS lookup for a given IP address using Python's socket module.
Intended for use in controlled, ethical environments.
"""

import socket


def reverse_dns_lookup(ip_address):
    """Perform a reverse DNS lookup for the given IP address."""
    try:
        hostname, _, ip_list = socket.gethostbyaddr(ip_address)
        return {
            "ip_address": ip_address,
            "hostname": hostname,
            "associated_ips": ip_list
        }
    except socket.herror as e:
        return {"error": f"Reverse DNS lookup failed: {str(e)}"}


def run(target):
    """Run the Reverse DNS Lookup module."""
    print(f"Performing reverse DNS lookup for: {target}")
    result = reverse_dns_lookup(target)

    if "error" in result:
        print(f" - Error: {result['error']}")
    else:
        print("\nReverse DNS Lookup Results:")
        print(f" - IP Address: {result['ip_address']}")
        print(f" - Hostname: {result['hostname']}")
        if result["associated_ips"]:
            print(f" - Associated IPs: {', '.join(result['associated_ips'])}")
        else:
            print(" - Associated IPs: None found")