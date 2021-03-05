import socket
import threading
import turtle
import alphabot
import time

server_ip = "127.0.0.1"
server_port = 7000

def client():
    robot = alphabot.AlphaBot()
    robot.setPWMA(100)
    robot.setPWMB(100)
    robot.stop()

    c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    c.connect((server_ip,server_port))
    
    while True:
        msg = input(">>")
        c.sendall(msg.encode())
        echo_msg = c.recv(4096).decode()

        print(f"ECHO>> {echo_msg}")
        _,path = echo_msg.split(',')

        print(path)

        index = 0
        while index < len(path):
            time.sleep(1.5)
            distance = ''
            if path[index] == 'F':
                index = index + 1
                while index < len(path) and path[index].isnumeric():
                    distance = distance + path[index]
                    index = index + 1
                
                robot.forward()
                time.sleep(1.5)
                robot.stop()


            elif path[index] == 'B':
                index = index + 1
                while index < len(path) and path[index].isnumeric():
                    distance = distance + path[index]
                    index = index + 1

                robot.backward()
                time.sleep(1.5)
                robot.stop()

            elif path[index] == 'L':
                index = index + 1
                while index < len(path) and path[index].isnumeric():
                    distance = distance + path[index]
                    index = index + 1

                robot.left()
                time.sleep(0.3)
                robot.stop()

            elif path[index] == 'R':
                index = index + 1
                while index < len(path) and path[index].isnumeric():
                    distance = distance + path[index]
                    index = index + 1

                robot.right()
                time.sleep(0.3)
                robot.stop()

        if msg == "close":
            break
    c.close()
    print("finito")
    


if __name__ == "__main__":
    client()