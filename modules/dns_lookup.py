import dns.resolver

def run(target):
    print(f"Running DNS Lookup for: {target}")
    try:
        for record_type in ['A', 'MX', 'TXT']:
            print(f"\n{record_type} Records:")
            answers = dns.resolver.resolve(target, record_type)
            for rdata in answers:
                print(f" - {rdata}")
    except Exception as e:
        print(f"Error performing DNS Lookup: {e}")