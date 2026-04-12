# SSL Certificate

## Description

The SSL Certificate module retrieves and parses SSL/TLS certificate data from a target host.

It provides key information about certificate validity, issuer, and subject details, which can be used to assess trust, ownership, and configuration of a secure service.

---

## How It Works

The module:

1. Accepts a domain name or URL as input  
2. Normalises the target to extract the hostname  
3. Establishes a secure socket connection to port 443  
4. Retrieves the SSL certificate from the remote host  
5. Parses certificate fields into a readable format  
6. Displays structured output and supports CSV export  

---

## Usage

### GUI

1. Open OSINTForge  
2. Select "SSL Certificate"  
3. Enter a domain or URL  
4. Click "Run SSL Lookup"  
5. (Optional) Export results using "Export as CSV"  

---

### CLI
```bash
python osintforge.py -m ssl_certificate -t example.com
```
---

## Example Output

Retrieving SSL certificate details for: example.com  

SSL Certificate Details:

Issuer:  
    commonName: Cloudflare Inc ECC CA-3  

Subject:  
    commonName: example.com  

Valid from: 2024-01-01 00:00:00  
Valid to: 2025-01-01 00:00:00  
Version: 3  
Serial number: 123456789  

---

## Output Explanation

- Issuer: Certificate authority that issued the certificate  
- Subject: Entity the certificate is issued to  
- Valid from / Valid to: Certificate validity period  
- Version: Certificate version  
- Serial number: Unique certificate identifier  

---

## Common Use Cases

- Verifying SSL/TLS configuration of a target domain  
- Identifying certificate authority and trust chain  
- Checking certificate expiration dates  
- Supporting infrastructure reconnaissance  

---

## Limitations

- Only supports standard HTTPS (port 443)  
- Does not validate full certificate chain  
- Does not detect misconfigurations beyond basic inspection  
- Requires network access to the target host  

---

## Future Improvements

- Support for custom ports  
- Certificate chain validation  
- Detection of weak or expired certificates  
- JSON export support  
- Integration with vulnerability databases  

---

## Ethical Considerations

SSL certificate data is publicly accessible, but should still be used responsibly.

This module should only be used for authorised security analysis or educational purposes.