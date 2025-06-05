from scapy.all import ARP, Ether, srp
target_ip = input("target(s): ")
#creates ARP packet
arp = ARP(pdst=target_ip)
#creates ethernet broadcast packet
#ff mac indicates broadcasting
ether = Ether(dst="ff:ff:ff:ff:ff:ff")
#stacks em
packet = ether/arp
result = srp(packet, timeout=3, verbose=1)[0]

#Clients list which will be filled from loop
clients = []
for sent, received in result:
    clients.append({'ip': received.psrc, 'mac': received_hwsrc})

print("Available Devices on the network:: ")
print("IP:" + " "*18+"MAC")
for client in clients:
    print("{:16}  {}".format(client['ip'], client['mac']))
