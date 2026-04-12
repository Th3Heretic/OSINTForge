# WHOIS Lookup

## Description

The WHOIS Lookup module retrieves domain registration information for a given domain.

It provides insight into domain ownership, registration details, and infrastructure, which can be useful during reconnaissance and OSINT investigations.

---

## How It Works

The module:

1. Accepts a domain name or URL as input  
2. Normalises the input to extract the domain  
3. Uses a WHOIS library to query registration data  
4. Parses and formats the returned information  
5. Displays results in a structured and readable format  

The module handles variations in WHOIS responses, including list-based and datetime fields.

---

## Usage

### GUI

1. Open OSINTForge  
2. Select "WHOIS Lookup"  
3. Enter a domain or URL  
4. Click "Run WHOIS Lookup"  

---

### CLI
```bash
python osintforge.py -m whois_lookup -t example.com
```
---

## Example Output

Performing WHOIS Lookup for: example.com  

WHOIS Lookup Results:

Domain Name: example.com  
Registrar: Example Registrar Ltd  
WHOIS Server: whois.example.com  
Creation Date: 2000-01-01 00:00:00  
Expiration Date: 2030-01-01 00:00:00  
Status: registered  
Name Servers: ns1.example.com, ns2.example.com  

---

## Output Explanation

- Domain Name: The registered domain  
- Registrar: Organisation responsible for domain registration  
- WHOIS Server: Server providing registration data  
- Creation Date: When the domain was first registered  
- Expiration Date: When the domain registration expires  
- Status: Current registration status  
- Name Servers: DNS servers associated with the domain  

---

## Common Use Cases

- Identifying domain ownership and registration details  
- Investigating domain lifecycle and expiration  
- Correlating infrastructure across multiple domains  
- Supporting reconnaissance during OSINT investigations  

---

## Limitations

- WHOIS data may be redacted due to privacy protections (e.g. GDPR)  
- Some fields may be missing or inconsistent depending on the registrar  
- Results depend on external WHOIS services  
- Rate limiting may occur with repeated queries  

---

## Future Improvements

- CSV/JSON export support  
- Batch domain processing  
- Integration with additional WHOIS data sources  
- Detection of suspicious or recently registered domains  

---

## Ethical Considerations

WHOIS data is publicly accessible but may contain sensitive or redacted information.

This module should only be used for authorised investigations or educational purposes, and in compliance with data protection regulations.