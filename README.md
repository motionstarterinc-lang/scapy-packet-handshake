Packet Handshake Toolkit

A small Python toolkit built with Scapy to explore raw packet crafting and TCP networking fundamentals hands-on, instead of just reading about them.

What it does:
send_ping() manually crafts and sends a raw ICMP Echo Request (the same thing the ping command does) and prints the reply. tcp_three_way_handshake() performs a full TCP 3-way handshake by hand, one packet at a time: SYN, then SYN-ACK, then ACK.

Why:
Built while studying networking fundamentals (TCP/IP, sockets, reliable data transfer) to see the theory actually happen on the wire instead of staying abstract. Paired with Wireshark packet capture and analysis to inspect both self-generated and live traffic.

Requirements:
Python 3. Scapy (pip install scapy). Run with admin or root privileges, since raw packet sending requires elevated permissions.

Usage:
Run "python packet_handshake.py" from the command line. By default it targets 192.168.1.1, a typical home router gateway. Change router_ip in the script to whatever target you have permission to test against.

Note: Only run this against devices or networks you own or have explicit permission to test. Sending crafted packets to systems you don't control without authorization is illegal.

Author: David Oladimejij, IT student at Towson University.
