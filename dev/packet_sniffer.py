from scapy.all import *

while(1):
    p=sniff(filter="mpls")
    print(p.dest)