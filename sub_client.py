import sys
import zmq
import uuid


port = "5556"  # default port
# ext arg for ports
if len(sys.argv) > 1:
    port =  sys.argv[1]
    int(port)

if len(sys.argv) > 2:
    port1 =  sys.argv[2]
    int(port1)
######  ZMQ
# Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)
print("Collecting updates from weather server...")
socket.connect ("tcp://localhost:%s" % port)
#########

if len(sys.argv) > 2:
    socket.connect ("tcp://localhost:%s" % port1)

# take same topic what we focus
t = '10001'
socket.setsockopt_string(zmq.SUBSCRIBE,t)

# take 5 time's msg from PUB
c_ID=uuid.uuid4()
print("client ID ",c_ID)
for update_nbr in range (5):
    string = socket.recv()
    print(string)
    topic, messagedata = string.split()
    # topic, messagesata = socket.recv_multipart()
    print(topic, messagedata)

     
    
