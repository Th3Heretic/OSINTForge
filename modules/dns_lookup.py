"""
dns_lookup.py

Performs DNS record lookups (A, MX, TXT) for a given domain using dnspython.
Intended for ethical use in controlled environments only.
"""

import dns.resolver


def run(target):
    print(f"Running DNS Lookup for: {target}")

    record_types = ['A', 'MX', 'TXT']
    results = []

    for record_type in record_types:
        print(f"\n{record_type} Records:")

        try:
            answers = dns.resolver.resolve(target, record_type)

            for rdata in answers:
                record_value = str(rdata)
                print(f" - {record_value}")

                results.append({
                    "type": record_type,
                    "value": record_value
                })

        except dns.resolver.NoAnswer:
            print(" - No answer for this record type.")

        except dns.resolver.NXDOMAIN:
            print(" - Domain does not exist.")
            break

        except dns.resolver.NoNameservers:
            print(" - No nameservers could be reached.")
            break

        except Exception as e:
            print(f" - Error retrieving {record_type} record: {e}")

    return results