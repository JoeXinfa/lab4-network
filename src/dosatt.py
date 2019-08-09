# python 2

from scapy.all import IP, TCP, send

def main():

    # Example from lecture 2019/8/9
    #p = IP(dst="slashdot.org")/TCP(dport=80)
    #a = scapy.IP(dst="slashdot.org")/TCP(dport=80)/"GET /HTTP/1.0\r\n\r\n"
    
    source_IP = "140.82.113.4" # www.github.com
    target_IP = "127.0.0.1" # localhost, the server
    source_port = 1000
    target_port = 8080
    i = 1

    #while True:
    while i < 10:
        source_port = 1000 * i
        my_ip = IP(src = source_IP, dst = target_IP)
	my_tcp = TCP(sport = source_port, dport = target_port)
	pkt = my_ip / my_tcp
	send(pkt, inter = .001)
	print "packet sent", i
	i = i + 1

if __name__ == "__main__":
    main()
