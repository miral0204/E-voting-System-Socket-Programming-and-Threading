import socket
import threading
import time

a=0
b=0
c=0
e=0

HEADER = 64
PORT = 5050 
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8' 
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    global a
    global b
    global c
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            elif int(msg)==1:
                a=a+1
            elif int(msg)==2:
                b=b+1
            elif int(msg)==3:
                c=c+1

            e = a + b + c
            print(f"[{addr}] {msg}")
            conn.send("Your Vote is Registered Succesfully".encode(FORMAT))
            if e>1:
                break
        if e>1:
            break
    conn.close()


def start():
    global a
    global b
    global c
    global d

    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1} ")
        d = a + b + c

        if int(d)>=3:
            break

print("[STARTING] server is starting...")
start()

if a==b and b==c:
    print("Tie between BJP, AAP and CONG")
elif a==b:
    if c>a:
        print("Winner is AAP")
    else:
        print ("Tie between BJP and AAP")
elif a==c:
    if b>a:
        print("Winner is AAP")
    else:
        print ("Tie between BJP and CONG")
elif b==c:
    if a>b:
        print("Winner is BJP")
    else:
        print ("Tie between AAP and CONG")
elif a>b:
    if a>c:
        print("Winner is BJP")
    else:
        print("Winner is CONG")
else:
    if b>c:
        print("Winner is AAP")
    else:
        print("Winner is CONG")