**OpenPort-Finder2.0**
The OpenPort-Finder2.0 is a Python script designed to find open ports on a specified IP address. The script uses the Scapy library to send a SYN packet to the target IP address and port, and then checks the response to determine whether the port is open or closed.

**Prerequisites**
Before running the OpenPort-Finder2.0 script, you must have the Scapy library installed. You can install Scapy using the following command:


pip install scapy




**Usage**
To use the OpenPort-Finder2.0 script, simply run the script and specify the target IP address and port. For example:


python OpenPort-Finder2.0.py 192.168.1.1 80

The script will then send a SYN packet to the specified IP address and port, and print a message indicating whether the port is open or closed.
