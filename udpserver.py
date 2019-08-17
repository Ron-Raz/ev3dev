import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
msg="xiu"
sock.bind(('192.168.2.1', 7777))
while True:
	(clientMsg, (clientIp, clientPort)) = sock.recvfrom(1000)
	print('clientMsg=',clientMsg,' clientIp=',clientIp,' clientPort=',clientPort)
#sock.sendto(msg.encode(), (ClientIP, ClientPort))
#print(ClientMsg)
sock.close()
