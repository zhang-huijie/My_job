#udp通信以客户端的身份
from socket import *
severName = 'hostname'
severPort = 12000
clientSocket = socket(AF_INET,SOCK_DGRAM)
message = raw_inpot('Input lowercasesentence:')
clientSocket.sendto(message.encode(),(severName,severPort))
modifiedMessage,serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
clientSocket.close()
