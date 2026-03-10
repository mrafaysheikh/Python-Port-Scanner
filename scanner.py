import nmap
from colorama import Fore, init
from pyfiglet import Figlet

init(autoreset=True)

# Banner
f = Figlet(font='slant')
print(Fore.RED + f.renderText('Port Scanner'))
print(Fore.GREEN + "Author  : Muhammad Rafay")
print("Mode    : Basic Network Recon")
print("="*50)

target = input("Enter Target IP: ")

scanner = nmap.PortScanner()

print(Fore.CYAN + f"\nScanning {target} (Top 1000 ports)...\n")

# Basic scan (Top ports only)
scanner.scan(target, arguments='-T4')

for host in scanner.all_hosts():
    print(Fore.YELLOW + f"\nHost: {host}")
    print(f"State: {scanner[host].state()}")

    for proto in scanner[host].all_protocols():
        print(Fore.CYAN + f"\nProtocol: {proto}")

        ports = sorted(scanner[host][proto].keys())

        for port in ports:
            state = scanner[host][proto][port]['state']
            service = scanner[host][proto][port]['name']

            if state == "open":
                color = Fore.GREEN
            else:
                color = Fore.WHITE

            print(color + f"Port {port:<5} | State: {state:<6} | Service: {service}")

print(Fore.YELLOW + "\nScan Completed.")

