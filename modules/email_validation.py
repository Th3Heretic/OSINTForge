import re
import dns.resolver

def run(target):
    print(f"Validating email address: {target}")

    try:
        # Validate email syntax
        if not is_valid_email(target):
            print("Error: Invalid email format.")
            return

        # Extract domain from email
        domain = target.split('@')[-1]

        # Check if domain has MX records
        if has_mx_record(domain):
            print(f"The domain '{domain}' has valid MX records.")
            print("Email address appears deliverable.")
        else:
            print(f"The domain '{domain}' does not have valid MX records.")
            print("Email address is not deliverable.")
    except Exception as e:
        print(f"Error during email validation: {e}")

def is_valid_email(email):
    # Basic regex for validating email format
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

def has_mx_record(domain):
    # Check if the domain has MX records
    try:
        answers = dns.resolver.resolve(domain, 'MX')
        return len(answers) > 0
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        return False