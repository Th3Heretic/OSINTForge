import whois

def run(target):
    print(f"Performing WHOIS Lookup for: {target}")

    try:
        # Perform WHOIS lookup
        domain_info = whois.whois(target)

        # Display relevant WHOIS information
        print("WHOIS Lookup Results:\n")
        print(f"Domain Name: {domain_info.domain_name}")
        print(f"Registrar: {domain_info.registrar}")
        print(f"WHOIS Server: {domain_info.whois_server}")
        print(f"Creation Date: {domain_info.creation_date}")
        print(f"Expiration Date: {domain_info.expiration_date}")
        print(f"Status: {domain_info.status}")
        print(f"Name Servers: {', '.join(domain_info.name_servers or [])}")
    except Exception as e:
        print(f"Error during WHOIS lookup: {e}")