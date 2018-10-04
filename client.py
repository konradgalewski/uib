import socket

TCP_IP="127.0.0.0"
TCP_PORT=5555
BUFFER_SIZE=1024
Message="Hell my, name is WHO?"

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP,TCP_PORT))
s.send(Message)
s.close
print("just send")
