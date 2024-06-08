import sys
import socket
import ipaddress

RED = "\33[91m"
BLUE = "\33[94m"
GREEN = "\033[32m"
YELLOW = "\033[93m"
PURPLE = '\033[0;35m' 
CYAN = "\033[36m"
END = "\033[0m"

banner = f"""	
	{YELLOW}
______          _     _____                                 
| ___ \        | |   /  ___|                                
| |_/ /__  _ __| |_  \ `--.  ___ __ _ _ __  _ __   ___ _ __ 
|  __/ _ \| '__| __|  `--. \/ __/ _` | '_ \| '_ \ / _ \ '__|
| | | (_) | |  | |_  /\__/ / (_| (_| | | | | | | |  __/ |   
\_|  \___/|_|   \__| \____/ \___\__,_|_| |_|_| |_|\___|_|   
                                	
        {RED}                        		-by Afnan	 
                                                 v1.0.0                          
"""

print(banner)

if len(sys.argv) == 2:
    target = sys.argv[1]  # Get the IP address or hostname from the command-line argument
    print("\033[93mScanning target:" +target)
    print("-" * 50)
    try:
        ipaddress.ip_address(target)  # Check if it's a valid IP address
    except ValueError:
        try:
            target = socket.gethostbyname(target)  # Translate the hostname to IPv4
        except socket.gaierror:
            print("Invalid hostname")
            sys.exit()
    ip_parts = target.split('.')
    last_octet = int(ip_parts[-1])  # Get the last octet as an integer

    if last_octet < 1 or last_octet > 255:
        print("Enter a valid IP address")
        sys.exit()

else:
    print("Invalid amount of arguments")
    print("Syntax: python3 portscanner.sh <ip>")
    sys.exit()

try:
    for port in range(50, 80):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is \33[91mopen")
        s.close()

except KeyboardInterrupt:
    print("\nExiting the scan")
    sys.exit()

except socket.error:
    print("\nCould not connect to server.")
    sys.exit()
 
