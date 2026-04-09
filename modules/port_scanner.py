"""
port_scanner.py

Performs a simple TCP connect-style port scan against a target host.
Designed for use in controlled environments only.
"""

import socket


def run(target, ports=None, timeout=1.0, verbose=True):
    """
    Run a simple port scan against `target`.

    :param target: hostname or IPv4 address (string)
    :param ports: optional iterable of port numbers to scan (ints)
    :param timeout: socket timeout in seconds
    :param verbose: show closed ports if True
    """
    print(f" - Performing Port Scanning for: {target}\n")

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

    # Handle custom ports
    if ports:
        try:
            if isinstance(ports, dict):
                port_map = ports
            else:
                port_map = {int(p): "" for p in ports}
        except Exception as e:
            print(f" - Error processing ports: {e}")
            return
    else:
        port_map = common_ports

    # Resolve target
    try:
        remote_ip = socket.gethostbyname(target)
        print(f" - Resolved {target} -> {remote_ip}\n")
    except socket.gaierror:
        print(f" - Error: could not resolve host '{target}'")
        return
    except Exception as e:
        print(f" - Unexpected resolution error: {e}")
        return

    open_ports = []

    # Scan ports
    for port, service in port_map.items():
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(timeout)
                result = s.connect_ex((remote_ip, int(port)))

                if result == 0:
                    svc = f" ({service})" if service else ""
                    print(f" - Port {port}{svc}: OPEN")
                    open_ports.append(port)
                elif verbose:
                    print(f" - Port {port}: closed/filtered")

        except Exception as e:
            print(f" - Error scanning port {port}: {e}")

    # Summary
    if not open_ports:
        print(" - No open ports found on scanned set.")
    else:
        print(f"\n - {len(open_ports)} open port(s) detected.")

    print("\n - Port scan complete.")