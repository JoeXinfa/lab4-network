import socket
import time

host = "www.baiwanzhan.com"
port = 80

def main():
    # TCP connect
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    
    # result socket_water.pcap
    #reqs = ["GET /service/site/search.aspx?query=water " \
    #    "HTTP/1.1\r\nHost:{}\r\n\r\n".format(host)]
    # result socket_falun.pcap
    #reqs = ["GET /service/site/search.aspx?query=%E6%B3%95%E8%BD%AE " \
    #    "HTTP/1.1\r\nHost:{}\r\n\r\n".format(host)]
    # result socket_water2.pcap
    reqs = ["GET /service/site/search.aspx?query=wa",
        "ter HTTP/1.1\r\nHost:{}\r\n\r\n".format(host)]
    # result socket_falun2.pcap
    #reqs = ["GET /service/site/search.aspx?query=%E6%B3%95",
    #    "%E8%BD%AE HTTP/1.1\r\nHost:{}\r\n\r\n".format(host)]
    print(reqs)

    requests = [info.encode() for info in reqs]
    responses = []
    for req in requests:
        client.send(req)
        resp = client.recv(4096)
        responses.append(repr(resp))
	time.sleep(15)

if __name__ == "__main__":
    main()
