import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
addr=('localhost',9000)
sock.connect(addr)
msg = sock.recv(1024)
print(msg.decode())

#이름을 문자열로 전송
myname = 'Jeongwon Choi'
sock.send(myname.encode())

#학번을 수신후 출력
msg = sock.recv(1024)
print(int.from_bytes(msg,'big'))
sock.close()