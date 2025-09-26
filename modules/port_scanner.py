"""
port_scanner.py

Performs a simple TCP connect-style port scan against a target host for a list
of common ports. Designed for use in controlled environments only.

Usage:
    from port_scanner import run
    run("example.com")             # uses default common ports
    run("192.0.2.1", ports=[80,443,8080])  # custom ports

Notes:
- This is a light, non-intrusive scanner (single-threaded by default).
- For larger scans or speed, a threaded/async approach can be added later.
"""

import socket

def run(target, ports=None, timeout=1.0):
    """
    Run a simple port scan against `target`.

    :param target: hostname or IPv4 address (string)
    :param ports: optional iterable of port numbers to scan (ints). If None,
                  a default set of common ports is used.
    :param timeout: socket timeout in seconds for each connection attempt.
    """
    print(f" - Performing Port Scanning for: {target}\n")

    # Default common ports (service name for nicer output)
    common_ports = {
        21: "FTP",
        22: "SSH",
        23: "Telnet",
        25: "SMTP",
        53: "DNS",
        80: "HTTP",
        110: "POP3",
        143: "IMAP",
        443: "HTTPS",
        3389: "RDP"
    }

    # If caller provided a custom ports list, convert to dict with empty names
    if ports:
        try:
            # allow list like [80,443] or dict-like mapping
            if isinstance(ports, dict):
                port_map = ports
            else:
                port_map = {int(p): "" for p in ports}
        except Exception as e:
            print(f" - Error processing provided ports list: {e}")
            return
    else:
        port_map = common_ports

    # Resolve hostname to IPv4 address (if needed)
    try:
        remote_ip = socket.gethostbyname(target)
        print(f" - Resolved {target} -> {remote_ip}\n")
    except socket.gaierror:
        print(f" - Error: could not resolve host '{target}'. Is the host correct?")
        return
    except Exception as e:
        print(f" - Unexpected error resolving host: {e}")
        return

    # Scan each port in port_map
    for port, service in port_map.items():
        s = None
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(timeout)
            result = s.connect_ex((remote_ip, int(port)))
            if result == 0:
                svc = f" ({service})" if service else ""
                print(f" - Port {port}{svc}: OPEN")
            else:
                # silent about closed to reduce noise, but log if you want
                print(f" - Port {port}: closed or filtered")
        except Exception as e:
            print(f" - Error scanning port {port}: {e}")
        finally:
            if s:
                try:
                    s.close()
                except Exception:
                    pass

    print("\n - Port scan complete.")