import socket

def run(target):
    print(f"Performing Port Scanning for: {target}\n")

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

    try:
        for port, service in common_ports.items():
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)  # 1-second timeout for each connection
                result = sock.connect_ex((target, port))
                if result == 0:
                    print(f"Port {port} ({service}): OPEN")
                sock.close()
            except Exception as e:
                print(f"Error scanning port {port}: {e}")
    except Exception as e:
        print(f"Error during port scanning: {e}")