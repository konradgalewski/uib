import socket

TCP_IP = "127.0.0.1"
TCP_PORT = 5555

message = "Hell my, name is WHO?"

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((TCP_IP,TCP_PORT))

while True:
    message= input()
    msg = bytes(message, 'utf-8')
    s.send(msg)

    if not message:
        break
    
    
s.close()
print("just send")
