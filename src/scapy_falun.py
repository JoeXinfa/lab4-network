# -*- coding: utf-8 -*-

from scapy.all import IP, TCP, send, conf, L3RawSocket, sr1
import os

"""
https://samsclass.info/123/proj14/p10-scapytcp.html
https://stackoverflow.com/questions/4750793/python-scapy-or-the-like-how-can-i-create-an-http-get-request-at-the-packet-leve

# How to run and look
sudo tcpdump -i any -w atest.pcap
sudo python this.py
Use Wireshark open the pcap file
"""

def main():

    os.system("sudo iptables -F")
    # This one drops all (anywhere source and destination)
    #os.system("sudo iptables -A OUTPUT -p tcp --tcp-flags RST RST -j DROP")
    # Drop all from source localhost
    os.system("sudo iptables -A OUTPUT -p tcp --tcp-flags RST RST -s 127.0.0.1 -j DROP")
    # Drop all from source 10.0.2.15 that is my IP address (ifconfig)
    os.system("sudo iptables -A OUTPUT -p tcp --tcp-flags RST RST -s 10.0.2.15 -j DROP")
    os.system("sudo iptables -L")

    # This is required for traffic to localhost
    conf.L3socket = L3RawSocket

    my_ip = IP(dst="www.baiwanzhan.com")
    my_tcp = TCP(dport=80)

    pkt = my_ip / my_tcp
    syn_ack = sr1(pkt) # client send SYN and receive SYN/ACK
    my_tcp = TCP(dport=80, sport=syn_ack[TCP].dport, seq=syn_ack[TCP].ack,
        ack=syn_ack[TCP].seq+1, flags='A')
    send(my_ip / my_tcp) # send ACK to complete the 3-way TCP handshake

    my_tcp.flags = 'AP'
    #my_tcp.show()

    get_str = "GET /service/site/search.aspx?query=法"
    request = my_ip / my_tcp / get_str
    send(request)
    print get_str

    get_str = "轮 HTTP/1.1\r\n" \
        "Host: www.baiwanzhan.com\r\n\r\n"
    request = my_ip / my_tcp / get_str
    send(request)
    print get_str

    #print type(reply)
    #reply.show()

if __name__ == "__main__":
    main()
