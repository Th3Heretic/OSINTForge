import argparse
from modules import dns_lookup, metadata_extraction, ip_geolocation, whois_lookup, subdomain_enum, port_scanner, website_metadata, email_validation, directory_scanner

def main():
    parser = argparse.ArgumentParser(description="OSINTForge - Modular OSINT Tool")
    parser.add_argument('-m', '--module', type=str, required=True, help="Module to run (e.g., dns_lookup, metadata_extraction, ip_geolocation, whois_lookup, subdomain_enum, port_scanner, website_metadata, email_validation, directory_scanner)")
    parser.add_argument('-t', '--target', type=str, required=True, help="Target for the module (e.g., domain, file path, email, or URL)")
    args = parser.parse_args()

    if args.module == 'dns_lookup':
        dns_lookup.run(args.target)
    elif args.module == 'metadata_extraction':
        metadata_extraction.run(args.target)
    elif args.module == 'ip_geolocation':
        ip_geolocation.run(args.target)
    elif args.module == 'whois_lookup':
        whois_lookup.run(args.target)
    elif args.module == 'subdomain_enum':
        subdomain_enum.run(args.target)
    elif args.module == 'port_scanner':
        port_scanner.run(args.target)
    elif args.module == 'website_metadata':
        website_metadata.run(args.target)
    elif args.module == 'email_validation':
        email_validation.run(args.target)
    elif args.module == 'directory_scanner':
        directory_scanner.run(args.target)
    else:
        print(f"Module '{args.module}' not found.")

if __name__ == "__main__":
    main()