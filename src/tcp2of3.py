from scapy.all import IP, TCP, send, conf, L3RawSocket, sr1

"""
https://samsclass.info/123/proj14/p10-scapytcp.html

# Drop all RST packets
sudo iptables -F
sudo iptables -A OUTPUT -p tcp --tcp-flags RST RST -j DROP
sudo iptables -L

sudo iptables -A OUTPUT -p tcp --tcp-flags RST RST -s <your-ip> -j DROP
ifconfig # find your IP address
sudo iptables -A OUTPUT -p tcp --tcp-flags RST RST -s 10.0.2.15 -j DROP

# How to run and look
sudo tcpdump -i any -w atest.pcap
sudo python this.py
Use Wireshark open the pcap file
"""

def main():
    # This is required for traffic to localhost
    conf.L3socket = L3RawSocket

    my_ip = IP(dst = "www.google.com")
    my_tcp = TCP(dport = 80)

    pkt = my_ip / my_tcp
    #send(pkt)
    sr1(pkt)

    print "packet sent"

if __name__ == "__main__":
    main()
