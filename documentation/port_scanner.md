# Port Scanner

## Description

The Port Scanner module performs a basic TCP connect scan against a target host to identify open ports.

It is designed to provide quick visibility into exposed services on a system using a lightweight and non-intrusive approach.

---

## How It Works

The module:

1. Accepts a hostname or IP address as input  
2. Resolves the target to an IPv4 address  
3. Iterates through a predefined or user-supplied list of ports  
4. Attempts a TCP connection to each port  
5. Reports ports that successfully accept connections  

Common ports are labelled with their associated services for clarity.

---

## Usage

### GUI

1. Open OSINTForge  
2. Select "Port Scanner"  
3. Enter a target domain or IP address  
4. Click "Run Port Scan"  

---

### CLI

python osintforge.py -m port_scanner -t example.com

---

## Example Output

Performing Port Scanning for: example.com  

Resolved example.com -> 93.184.216.34  

Port 80 (HTTP): OPEN  
Port 443 (HTTPS): OPEN  

2 open port(s) detected.  

Port scan complete.

---

## Default Ports Scanned

- 21 (FTP)  
- 22 (SSH)  
- 23 (Telnet)  
- 25 (SMTP)  
- 53 (DNS)  
- 80 (HTTP)  
- 110 (POP3)  
- 143 (IMAP)  
- 443 (HTTPS)  
- 3389 (RDP)  

---

## Limitations

- Only performs TCP connect scans (no SYN or stealth scanning)  
- Does not perform service/version detection  
- May miss filtered or rate-limited ports  
- Scan speed depends on network latency and timeout settings  

---

## Future Improvements

- Multi-threaded scanning for improved performance  
- Custom port range input in GUI  
- Service fingerprinting and banner grabbing  
- UDP scanning support  
- CSV/JSON export functionality  

---

## Ethical Considerations

Port scanning can be considered intrusive depending on the target.

This module should only be used on systems you own or have explicit permission to test.

Unauthorised scanning may violate laws or network policies.