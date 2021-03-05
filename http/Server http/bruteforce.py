import socket

server_ip = "127.0.0.1"
server_port = 5000

def client():
    c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    c.connect((server_ip,server_port))

    while True:


        body = "username=bagnis&password=gabriele"
        msg = f"POST http://127.0.0.1:5000 HTTP/1.1\nHost:localhost:5000\nContent_Type=application/x-www-form-urlencoded\nContent_Length={len(body)}\n\n"+body
        print(f"sending:\n\n{msg}\n\n")
        c.sendall(msg.encode())
        echo_msg = c.recv(4096)
        print(f"ECHO>> {echo_msg}")
        if len(echo_msg) > 0:
            break
    
    c.close()

if __name__ == "__main__":
    client()