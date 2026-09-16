"""
packet_handshake.py

A small hands-on networking toolkit built with Scapy to demonstrate raw
packet crafting and the TCP 3-way handshake at the byte level.

Note: for readability this demo assumes a reply is received. In production
code you would check for None before accessing reply fields.

Author: David Oladimejij
"""

from scapy.all import IP, ICMP, TCP, sr1, send


def send_ping(target_ip):
  packet = IP(dst=target_ip) / ICMP()
  reply = sr1(packet, timeout=2)
  reply.show()
  return reply


def tcp_three_way_handshake(target_ip, target_port=80):
  syn = IP(dst=target_ip) / TCP(dport=target_port, flags="S")
  syn_ack = sr1(syn, timeout=2)
  print("Received SYN-ACK:")
  syn_ack.show()
  ack = IP(dst=target_ip) / TCP(dport=target_port, sport=syn.sport, seq=syn_ack.ack, ack=syn_ack.seq + 1, flags="A")
  send(ack)
  print("Handshake complete with " + target_ip)
  return syn_ack


if __name__ == "__main__":
  router_ip = "192.168.1.1"
  print("--- ICMP Ping ---")
  send_ping(router_ip)
  print("--- TCP 3-Way Handshake ---")
  tcp_three_way_handshake(router_ip, target_port=80)
  
