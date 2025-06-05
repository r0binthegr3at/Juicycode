import os, platform
from datetime import datetime
net = raw_input("Enter IP>: ")
net1 = net.split('.')
a = '.'
net2 = net1[0]+a+net1[1]+a+net1[2]+a
st1 = int(raw_input("Starting number>: "))
en1 = int(raw_input("Last number>: "))
en1=en1+1
oper = platform.system()
if (oper=='Windows'):
    ping1 = "ping -n 1 "
elif (oper=='Linux'):
    ping1 = "ping -c 1 "
else:
    ping1 = "ping -c 1 "
t1 = datetime.now()
print("Scanning in process")
for ip in xrange(st1,en1):
    addr = net2+str(ip)
    comm = ping1+adr
    response = os.popen(comm)
    print(response.readlines())
    list1 = response.readlines()[:]
    for line in list1:
        if(line.count("TTL")):
            print("hello")
            print(addr, "--> Live")
            break

t2 = datetime.now()
total = t2-t1
print("Scanning done in>: ", total)
