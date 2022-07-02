import sys
from scapy.layers.inet import IP, ICMP
from scapy.sendrecv import sr
src=input("Enter destination address... ")
dst=input("Enter destination address... ")

ans, unas =sr(IP(dst)/ICMP(),timeout=3) 
