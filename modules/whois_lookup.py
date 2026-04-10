import whois
from datetime import datetime
from urllib.parse import urlparse


def _normalise_target(target: str) -> str:
    target = target.strip()

    if target.startswith(("http://", "https://")):
        parsed = urlparse(target)
        return parsed.netloc

    return target


def _clean_field(value):
    """
    Normalise WHOIS fields:
    - Handle lists (take first or join where needed)
    - Handle None
    """
    if isinstance(value, list):
        return value[0] if value else "N/A"
    return value if value else "N/A"


def _format_date(value):
    if isinstance(value, list):
        value = value[0] if value else None

    if isinstance(value, datetime):
        return value.strftime("%Y-%m-%d %H:%M:%S")

    return value if value else "N/A"


def run(target):
    output = []

    target = _normalise_target(target)
    output.append(f"Performing WHOIS Lookup for: {target}")

    try:
        domain_info = whois.whois(target)

        output.append("\nWHOIS Lookup Results:\n")

        output.append(f"Domain Name: {_clean_field(domain_info.domain_name)}")
        output.append(f"Registrar: {_clean_field(domain_info.registrar)}")
        output.append(f"WHOIS Server: {_clean_field(domain_info.whois_server)}")
        output.append(f"Creation Date: {_format_date(domain_info.creation_date)}")
        output.append(f"Expiration Date: {_format_date(domain_info.expiration_date)}")

        status = domain_info.status
        if isinstance(status, list):
            status = ", ".join(status)
        output.append(f"Status: {status if status else 'N/A'}")

        name_servers = domain_info.name_servers
        if isinstance(name_servers, list):
            name_servers = ", ".join(sorted(set(ns.lower() for ns in name_servers)))
        output.append(f"Name Servers: {name_servers if name_servers else 'N/A'}")

    except Exception as e:
        output.append(f"[ERROR] WHOIS lookup failed: {e}")

    return "\n".join(output)