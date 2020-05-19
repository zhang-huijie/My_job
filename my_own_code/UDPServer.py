#udp通信按照服务器的方式需要在两个主机上面运行程序
from socket import *
severPort = 12000
serverSockert = socket(AF_INET,SOCK_DGRAM)
serverSockert.bind('',severPort)
print("The server id ready to receive")
while True:
    message,clientAddress = serverSockert.recvfrom(2048)
    modifiedMessage = message.decode().upper()
    serverSockert.sendto(modifiedMessage.encode(),clientAddress)