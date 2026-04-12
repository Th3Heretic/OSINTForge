# Reverse DNS

## Description

The Reverse DNS module performs a reverse DNS lookup on a given IP address to retrieve the associated hostname.

This is useful for identifying the domain or service linked to a public IP address.

---

## How It Works

The module:

1. Accepts an IP address as input  
2. Uses Python’s socket library to perform a reverse lookup  
3. Queries DNS for PTR (Pointer) records  
4. Returns the resolved hostname and associated IPs (if available)  

---

## Usage

### GUI

1. Open OSINTForge  
2. Select "Reverse DNS"  
3. Enter a target IP address  
4. Click "Run Reverse DNS"  

---

### CLI
```bash
python osintforge.py -m reverse_dns -t 8.8.8.8
```

---

## Example Output

Performing reverse DNS lookup for: 8.8.8.8  

Reverse DNS Lookup Results:  
IP Address: 8.8.8.8  
Hostname: dns.google  
Associated IPs: 8.8.8.8  

---

## Common Use Cases

- Identifying the hostname behind a public IP address  
- Verifying ownership or service association of an IP  
- Supporting reconnaissance during authorised investigations  
- Correlating infrastructure between domains and IPs  

---

## Limitations

- Requires a valid IP address as input  
- Private or internal IPs (e.g. 192.168.x.x, 10.x.x.x) typically do not resolve  
- Some public IPs may not have PTR records configured  
- Results depend on DNS configuration and availability  

---

## Future Improvements

- Batch processing of multiple IP addresses  
- CSV/JSON export functionality  
- Improved handling of IPv6 addresses  
- Integration with additional DNS intelligence sources  

---

## Ethical Considerations

Reverse DNS lookups are generally passive, but should still be used responsibly.

This module should only be used for authorised investigations or educational purposes.