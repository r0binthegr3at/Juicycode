import nmap
scanner = nmap.PortScanner()
target = input("<target(s)>:")
options = "-sS -sV -O -A -p 1-1000"
# -O is OS detection, -sS is TCPSYN scan, -sV version detect, A is aggressive scan

scanner.scan(target, arguments=options)
for host in scanner.all_hosts():
    print("Host: ", host)
    print("State: ", scanner[host].state())
    for proto in scanner[host].all_protocols():
        print("Protocol: ", proto)
        ports = scanner[host][proto].keys()
        for port in ports:
            print("Port: ", port, "State: ", scanner[host][proto][port]['state'])

