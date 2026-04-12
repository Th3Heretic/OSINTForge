# Traceroute

## Description

The Traceroute module maps the network path between the local system and a target host.

It identifies each hop along the route, providing insight into network structure, routing behaviour, and potential bottlenecks.

---

## How It Works

The module:

1. Accepts a hostname or IP address as input  
2. Resolves the target to an IP address  
3. Sends packets with incrementing Time-To-Live (TTL) values  
4. Receives responses from intermediate routers  
5. Records each hop along the route to the destination  
6. Executes the process in a background thread to prevent GUI freezing  

The module has been optimised to improve stability and avoid application crashes during execution.

---

## Usage

### GUI

1. Open OSINTForge  
2. Select "Traceroute"  
3. Enter a target domain or IP address  
4. Click "Run Traceroute"  

---

### CLI
```bash
python osintforge.py -m traceroute -t example.com
```
---

## Example Output

Running traceroute for: example.com  

Hop 1: 192.168.0.1  
Hop 2: 10.10.0.1  
Hop 3: 172.16.0.5  
Hop 4: 93.184.216.34  

Traceroute complete.

---

## Common Use Cases

- Analysing network routing paths  
- Identifying latency or routing issues  
- Mapping infrastructure between systems  
- Supporting network diagnostics and investigations  

---

## Limitations

- Results may vary depending on network conditions  
- Some routers may block or ignore traceroute packets  
- Intermediate hops may not respond, resulting in incomplete paths  
- Accuracy depends on underlying network behaviour  

---

## Performance Notes

- Runs in a background thread to prevent GUI freezing  
- Designed to avoid application crashes during long-running operations  
- Execution time depends on network latency and hop count  

---

## Future Improvements

- Visual representation of network paths  
- Latency measurement per hop  
- IPv6 support  
- Export results to CSV/JSON  
- Enhanced error handling and retry logic  

---

## Ethical Considerations

Traceroute should only be used for authorised network analysis.

Repeated probing of networks without permission may be considered intrusive or violate acceptable use policies.