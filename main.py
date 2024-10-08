#!/usr/bin/env python3

import socket
import argparse
def display_banner():
    banner = """
     ________  ________  ________  _________        ________  ________  ________  ________      
|\   __  \|\   __  \|\   __  \|\___   ___\     |\   ____\|\   ____\|\   __  \|\   ___  \    
\ \  \|\  \ \  \|\  \ \  \|\  \|___ \  \_|     \ \  \___|\ \  \___|\ \  \|\  \ \  \\ \  \   
 \ \   ____\ \  \\\  \ \   _  _\   \ \  \       \ \_____  \ \  \    \ \   __  \ \  \\ \  \  
  \ \  \___|\ \  \\\  \ \  \\  \|   \ \  \       \|____|\  \ \  \____\ \  \ \  \ \  \\ \  \ 
   \ \__\    \ \_______\ \__\\ _\    \ \__\        ____\_\  \ \_______\ \__\ \__\ \__\\ \__\
    \|__|     \|_______|\|__|\|__|    \|__|       |\_________\|_______|\|__|\|__|\|__| \|__|
                                                  \|_________|                              
                                                                                            
                                                                                            
    """
    print(banner)

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Timeout after 1 second
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port} is open")
        sock.close()
    except Exception as e:
        print(f"Error scanning port {port}: {e}")

def main():
    display_banner()
    parser = argparse.ArgumentParser(description="Port Scanner")
    parser.add_argument("ip", type=str, help="IP address to scan")
    parser.add_argument("--start_port", type=int, default=1, help="Start port range (default: 1)")
    parser.add_argument("--end_port", type=int, default=1024, help="End port range (default: 1024)")
    args = parser.parse_args()

    ip = args.ip
    start_port = args.start_port
    end_port = args.end_port

    print(f"Scanning {ip} from port {start_port} to {end_port}...")

    for port in range(start_port, end_port + 1):
        scan_port(ip, port)

if __name__ == "__main__":
    main()
