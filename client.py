import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.246.225"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)

    client.send(message)
    print(client.recv(2048).decode(FORMAT))

print("t\t     * * * * * LIST OF CANDIDATES * * * * * \n\n\n")
print("\t\t\t       NAME                         SYMBOL\n\n")
print("\t\t\t 1.Mamata Banerjee --> BJP               1.Fish\n")
print("\t\t\t 2.Deepa Dasmunsi  -->AAP                2.Boat\n")
print("\t\t\t 3.Protima Rajak   -->CONG               3.Motorcycle\n")
a=input("Enter your Respective vote:  ")

if int(a)==1 or int(a)==2 or int(a)==3:
    send(a)
else:
    send(DISCONNECT_MESSAGE)
send(DISCONNECT_MESSAGE)