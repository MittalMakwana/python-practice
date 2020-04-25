import socket

def scanner(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((host, port))
        return True
    except:
        return False

for i in range(1,100):
    if scanner('localhost', i):
        print('port :' , i)


