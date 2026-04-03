from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost',3335))


print('HW3 - TCP Calculator')

while True:
    msg = input('Enter Calculation formula\n')
    if(msg == 'q'):
        break

    s.send(msg.encode())

    
    print(s.recv(1024).decode())

s.close()
    

      