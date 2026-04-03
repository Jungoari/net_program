from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.bind(('',3335))
s.listen(1)

print('Waiting...')

while True:
    client, addr = s.accept()
    print('Connection from ', addr)
    while True:
        data = client.recv(1024)
        
        if not data:
            break

        data = data.decode()
        num1, op, num2 = data.split() # 공백을 기준으로 나누기
        num1 = int(num1)
        num2 = int(num2)

        if(op == '+'):
            result = num1 + num2
        elif(op == '-'):
            result = num1 - num2
        elif(op == '*'):
            result = num1 * num2
        elif(op == '/'):
            result = num1 / num2
            result = round(result,1)
        else:
            client.send(b'Wrong Operator')
            
        client.send(str(result).encode())
        
        
    client.close()
