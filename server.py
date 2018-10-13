import socket

TCP_IP="127.0.0.1"
TCP_PORT=5555
BUFFER_SIZE=1024

s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((TCP_IP,TCP_PORT))
#s.listen(1)
#con, adres = s.accept()
#print("conneted to adr", adres)
while True:
    
    data = s.recv(BUFFER_SIZE)
    
    if not data:
        break
    print("received", data)
    
s.close()
