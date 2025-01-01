import ipaddress
import subprocess
from concurrent.futures import ThreadPoolExecutor

def ping_ip(ip):
    """Ping an IP address to check if it's alive."""
    try:
        # 'ping' command (-c 1 for one packet, -W 1 for a 1-second timeout)
        result = subprocess.run(
            ["ping", "-c", "1", "-W", "1", str(ip)],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        if result.returncode == 0:
            print(f"[+] {ip} is alive")
            return ip
    except Exception as e:
        print(f"Error pinging {ip}: {e}")
    return None

def main():
    subnet = input("Enter the subnet (e.g., 192.168.1.0/24): ")
    try:
        # Generate all IPs in the subnet
        network = ipaddress.ip_network(subnet, strict=False)
        print(f"Scanning subnet {subnet}...\n")

        live_hosts = []
        with ThreadPoolExecutor(max_workers=50) as executor:
            # Ping all hosts in parallel
            results = executor.map(ping_ip, network.hosts())
            live_hosts = [ip for ip in results if ip]

        print("\nScan complete!")
        if live_hosts:
            print("Live hosts:")
            for host in live_hosts:
                print(host)
        else:
            print("No live hosts found.")

    except ValueError:
        print("Invalid subnet format. Please use CIDR notation (e.g., 192.168.1.0/24).")

if __name__ == "__main__":
    main()
