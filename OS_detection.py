import nmap, sys
syntax="OS_detection.py <hostname/IP addr>"
if len(sys.argv) == 1:
    print(syntax)
    sys.exit()

host = sys.argv[1]
nm=nmap.PortScanner()
open_ports_dict = nm.scan(host, arguments="-O").get("scan").get(host).get("tcp")
print("open_ports" + "Description")
port_list = open_ports_dicts.keys()
port_list.sort()
for port in port_list:
    print(port, "---\t-->", open_ports_dict.get(port)[name])
print("\n---------------OS-DETAILS----------------------\n")
print("Details about scanned host are: \t", nm[host]['osmatch'][0]['osclass'][0]['cpe'])
print("OS Family is: \t\t", nm[host]['osmatch'][0]['osclass'][0]['osfamily'])
print("Type of OS: \t\t\t",nm[host]['osmatch'][0]['osclass'][0]['type'])
print("OS generarion: \t", nm[host]['osmatch'][0]['osclass'][0]['osgen'])
print("OS Vendor: \t\t", nm[host]['osmatch'][0]['osclass'][0]['vendor'])
print("Accuracy of detection is: \t\t", nm[host]['osmatch'][0]['osclass'][0]['accuracy'])
