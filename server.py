import os
from socket import *
from urllib.parse import unquote, urlparse

base_dir = os.path.dirname(os.path.abspath(__file__))

s = socket()
s.bind(('', 80))
s.listen(10)

while True:
    c, addr = s.accept()
    try:
        data = c.recv(1024)
        if not data:
            c.close()
            continue

        msg = data.decode(errors='ignore')
        req = msg.split('\r\n')
        request_line = req[0].split(' ')
        path = request_line[1] if len(request_line) > 1 else '/'
        path = unquote(urlparse(path).path)
        filename = path.lstrip('/')

        if filename.endswith('/'):
            filename = filename.rstrip('/')
        if filename == '':
            filename = 'index.html'

        filepath = os.path.join(base_dir, filename)

        if filename == 'index.html':
            f = open(filepath, 'r', encoding='utf-8')
            mimeType = 'text/html; charset=utf-8'
        elif filename == 'iot.png':
            f = open(filepath, 'rb')
            mimeType = 'image/png'
        elif filename == 'favicon.ico':
            f = open(filepath, 'rb')
            mimeType = 'image/x-icon'
        else:
            raise FileNotFoundError

        header = 'HTTP/1.1 200 OK\r\n'
        header += 'Content-Type: ' + mimeType + '\r\n\r\n'
        c.send(header.encode())

        response_data = f.read()
        if filename == 'index.html':
            c.send(response_data.encode())
        else:
            c.send(response_data)
        f.close()

    except (FileNotFoundError, IndexError):
        if 'filename' in locals():
            print(f"File Not Found: {filename}")
        else:
            print('Malformed request received')
        header = 'HTTP/1.1 404 Not Found\r\n\r\n'
        body = '<HTML><HEAD><TITLE>Not Found</TITLE></HEAD>'
        body += '<BODY>Not Found</BODY></HTML>'
        c.send(header.encode() + body.encode())

    finally:
        c.close()