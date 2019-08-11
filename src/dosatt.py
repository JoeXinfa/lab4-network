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

    source_IP = "10.0.2.15" # spoof
    target_IP = "127.0.0.1" # localhost
    target_port = 8080
    i = 1

    #while True:
    while i < 8000:
        my_ip = IP(src=source_IP, dst=target_IP)
        #my_ip = IP(dst=target_IP)
	my_tcp = TCP(sport=i, dport=target_port)
	pkt = my_ip / my_tcp
        sr1(pkt)
	print "packet sent", i
	i = i + 1

if __name__ == "__main__":
    main()
