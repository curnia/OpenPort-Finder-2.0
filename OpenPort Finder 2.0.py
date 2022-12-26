import scapy
from scapy.all import *

# define the target IP address and port
target_ip = "192.168.1.1"
target_port = 80

# create a SYN packet
packet = IP(dst=target_ip)/TCP(dport=target_port, flags="S")

# send the packet and receive the response
response = sr1(packet, verbose=False)

# if the response is not None, the port is open
if response:
  print(f"Port {target_port} is open")

# if the response is None, the port is closed
else:
  print(f"Port {target_port} is closed")