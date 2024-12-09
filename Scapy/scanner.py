import sys
from scapy.all import *
from scapy.layers.l2 import Ether, ARP

if len(sys.argv) !=2:
    print("Using : Python scanner.py 192.168.100.0/24")
    sys.exit(1)
try:
    alive, dead = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=sys.argv[1]), timeout=2, verbose=0)
    print("MAC ADDRESS - IP ADDRESS")
    for i in range(0, len(alive)):
        print(alive[i][1].hwsrc + "--" + alive[i][1].psrc)
except:
    pass