import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('',9000))
s.listen(2)

while True:
    client, addr = s.accept()
    print('Connection from ',addr)
    client.send(b'Hello '+ addr[0].encode())

    #학생 이름 수신후 출력

    msg = client.recv(1024)
    print(msg.decode())

    #학생 학번 전송
    student_id = 20211524
    client.send(student_id.to_bytes(4,'big'))

    client.close()