# Subdomain Enumeration

## Description

The Subdomain Enumeration module performs wordlist-based discovery of subdomains associated with a target domain.

It identifies valid subdomains by attempting DNS resolution and reporting those that successfully resolve to IP addresses.

---

## How It Works

The module:

1. Accepts a domain name as input  
2. Loads a local wordlist of potential subdomains  
3. Generates candidate subdomains (e.g. admin.example.com)  
4. Uses DNS resolution to check if each subdomain exists  
5. Executes lookups using multi-threading for improved performance  
6. Filters and reports only successfully resolved subdomains  

The module also includes wildcard DNS detection to prevent false positives.

---

## Usage

### GUI

1. Open OSINTForge  
2. Select "Subdomain Enumeration"  
3. Enter a target domain  
4. Click "Run Subdomain Enumeration"  

---

### CLI
```bash
python osintforge.py -m subdomain_enum -t example.com
```
---

## Example Output

Running subdomain enumeration for: example.com  

Found: admin.example.com -> 192.168.1.1  
Found: mail.example.com -> 192.168.1.2  

Enumeration complete. 2 subdomains discovered.

---

## Wildcard DNS Detection

Some domains resolve all subdomains to the same IP address (wildcard DNS).

The module detects this by testing random subdomains.  
If wildcard behaviour is detected, enumeration is stopped to avoid misleading results.

Example:

Wildcard DNS appears to be present.  
Aborting brute-force enumeration to avoid false positives.

---

## Common Use Cases

- Discovering hidden or undocumented subdomains  
- Mapping an organisation’s attack surface  
- Identifying services such as mail, admin panels, or APIs  
- Supporting reconnaissance during authorised security testing  

---

## Limitations

- Relies on a static local wordlist  
- Does not detect subdomains not present in the wordlist  
- DNS responses may be affected by caching or rate limiting  
- Some subdomains may exist but not resolve publicly  

---

## Future Improvements

- Support for custom wordlists via GUI  
- Integration with passive OSINT sources (e.g. certificate transparency logs)  
- Recursive subdomain discovery  
- CSV/JSON export support  
- Adjustable thread count  

---

## Ethical Considerations

Subdomain enumeration should only be conducted against systems you are authorised to assess.

Unauthorised scanning may violate acceptable use policies or legal regulations.