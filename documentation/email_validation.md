# [DEPRECATED]
# Email Validation

## Description

The Email Validation module performs basic checks on an email address to determine whether it is correctly formatted and whether the associated domain can receive emails.

It combines syntax validation with DNS-based checks to provide an initial assessment of validity.

---

## How It Works

The module performs two checks:

1. Syntax Validation  
   Ensures the email follows a valid structure (e.g. username@domain.com)

2. Domain Validation (MX Records)  
   Queries DNS for MX records to confirm the domain can receive email

---

## Usage

### GUI

1. Open OSINTForge  
2. Select Email Validation (if enabled)  
3. Enter an email address  
4. Click "Run Email Validation"  

---

### CLI
```bash
python osintforge.py -m email_validation -t test@example.com
```

#### Example Output
```bash
Valid email:

Validating email address: test@example.com  
The domain 'example.com' has valid MX records.  
Email address appears deliverable.
```

Invalid format:
```bash
Validating email address: invalid_email  
Error: Invalid email format.
```

---

## Limitations

- Does not guarantee mailbox existence  
- Some domains block MX queries or use catch-all configurations  
- Cannot detect disabled or inactive inboxes  

---

## Future Improvements

- SMTP verification (with safe handling)  
- Catch-all domain detection  
- Integration with breach datasets or OSINT sources  
- Bulk email validation support  

---

## Ethical Considerations

Email validation should only be used for legitimate and authorised purposes.

Avoid excessive or automated querying against domains that may interpret this behaviour as abusive.

This module is intended for educational, defensive, and investigative use only.