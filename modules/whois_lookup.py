import whois

import sys
from io import StringIO

def run(target):
    output = []
    output.append(f"Performing WHOIS Lookup for: {target}")

    try:
        # Perform WHOIS lookup
        domain_info = whois.whois(target)

        # Collect WHOIS information
        output.append("WHOIS Lookup Results:\n")
        output.append(f"Domain Name: {domain_info.domain_name}")
        output.append(f"Registrar: {domain_info.registrar}")
        output.append(f"WHOIS Server: {domain_info.whois_server}")
        output.append(f"Creation Date: {domain_info.creation_date}")
        output.append(f"Expiration Date: {domain_info.expiration_date}")
        output.append(f"Status: {domain_info.status}")
        name_servers = ', '.join(domain_info.name_servers or []) if domain_info.name_servers else "N/A"
        output.append(f"Name Servers: {name_servers}")

    except Exception as e:
        output.append(f"Error during WHOIS lookup: {e}")

    return "\n".join(output)