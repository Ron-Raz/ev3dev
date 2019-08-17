import socket
sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
msg="oi"
sock.sendto(msg.encode(), ("192.168.2.1", 7777))
(ServerMsg, (ServerIP, ServerPort)) = sock.recvfrom(1000)
print(ServerMsg)
sock.close()

