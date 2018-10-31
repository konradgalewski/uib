import sys
import zmq
import uuid
import json
import random
import time


port_RX = '5556'  # port PULL
port_TX = '5557'  #port PUSH

######  ZMQ
# Socket to talk to server
c_ID=str(uuid.uuid4())
print(str(c_ID))
#c_ID=random.randrange(1,1000)

print("client / worker ID ",c_ID)

context = zmq.Context()
consumer_RX = context.socket(zmq.PULL)
consumer_RX.connect("tcp://127.0.0.1:5556")
#########

consumer_TX = context.socket(zmq.PUSH)
consumer_TX.connect("tcp://127.0.0.1:5557")

while True:
    work=consumer_RX.recv_json()
    print("from producer ",work)
    data = work['num']
    result = {'consumer':c_ID,'num':data}
    print(result)
#    if data==0:
    consumer_TX.send_json(result)
    print(result)
    time.sleep(1)


    
