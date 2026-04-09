"""
reverse_dns.py

Performs a reverse DNS lookup for a given IP address using Python's socket module.
Intended for use in controlled, ethical environments.
"""

from __future__ import annotations

import ipaddress
import socket


def _is_valid_ip(value: str) -> bool:
    """
    Validate whether the supplied value is a valid IPv4 or IPv6 address.
    """
    try:
        ipaddress.ip_address(value)
        return True
    except ValueError:
        return False


def reverse_dns_lookup(ip_address: str) -> dict:
    """
    Perform a reverse DNS lookup for the given IP address.
    """
    if not _is_valid_ip(ip_address):
        return {"error": "Invalid IP address format."}

    try:
        hostname, aliases, ip_list = socket.gethostbyaddr(ip_address)
        return {
            "ip_address": ip_address,
            "hostname": hostname,
            "aliases": aliases,
            "associated_ips": ip_list
        }

    except socket.herror:
        return {
            "ip_address": ip_address,
            "no_ptr": True,
            "message": "No PTR record found for this IP address."
        }

    except Exception as exc:
        return {"error": f"Unexpected reverse DNS error: {exc}"}


def run(target: str) -> None:
    """
    Run the Reverse DNS Lookup module.
    """
    print(f" - Performing reverse DNS lookup for: {target}")

    result = reverse_dns_lookup(target)

    if "error" in result:
        print(f" - Error: {result['error']}")
        return

    if result.get("no_ptr"):
        print(f" - IP Address: {result['ip_address']}")
        print(f" - Result: {result['message']}")
        return

    print("\n - Reverse DNS Lookup Results:")
    print(f" - IP Address: {result['ip_address']}")
    print(f" - Hostname: {result['hostname']}")

    aliases = result.get("aliases", [])
    if aliases:
        print(f" - Aliases: {', '.join(aliases)}")
    else:
        print(" - Aliases: None found")

    associated_ips = result.get("associated_ips", [])
    if associated_ips:
        print(f" - Associated IPs: {', '.join(associated_ips)}")
    else:
        print(" - Associated IPs: None found")