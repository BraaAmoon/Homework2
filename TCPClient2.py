import socket
cs=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
cs.settimeout(150)
try:
    cs.connect(('127.0.0.1',7777))

    while True:
        data = cs.recv(1024).decode()
        print(data)
        req=input()
        cs.sendall(req.encode())

except socket.error as err:
    print(err)
finally:
    cs.close()
print('end')