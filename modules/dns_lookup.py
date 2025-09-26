"""
dns_lookup.py

Performs DNS record lookups (A, MX, TXT) for a given domain using dnspython.
Intended for ethical use in controlled environments only.
"""

import dns.resolver

def run(target):
    # Print the domain for which DNS lookup is being performed
    print(f"Running DNS Lookup for: {target}")
    record_types = ['A', 'MX', 'TXT']

    # Iterate over each DNS record type to query
    for record_type in record_types:
        print(f"\n{record_type} Records:")
        try:
            # Attempt to resolve the DNS records of the given type
            answers = dns.resolver.resolve(target, record_type)
            for rdata in answers:
                print(f" - {rdata}")
        except dns.resolver.NoAnswer:
            # No records of this type found for the domain
            print(" - No answer for this record type.")
        except dns.resolver.NXDOMAIN:
            # Domain does not exist
            print(" - Domain does not exist.")
            break
        except dns.resolver.NoNameservers:
            # No nameservers could be reached to resolve the query
            print(" - No nameservers could be reached.")
            break
        except Exception as e:
            # Catch-all for any other exceptions
            print(f" - Error retrieving {record_type} record: {e}")