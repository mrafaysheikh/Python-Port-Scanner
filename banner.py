import socket

def grab_banner(ip, port):
    try:
        sock = socket.socket()
        sock.settimeout(2)
        sock.connect((ip, port))
        banner = sock.recv(1024)
        return banner.decode().strip()
    except:
        return "No Banner"
