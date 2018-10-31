import sys
import zmq
import uuid
import json
import random
import time


port_RX = '5556'  # port PULL # TODO: PEP8
port_TX = '5557'  #port PUSH  # TODO: PEP8

######  ZMQ
# Socket to talk to server
c_ID=str(uuid.uuid4()) # TODO: PEP8
print(str(c_ID)) # TODO: PEP8
#c_ID=random.randrange(1,1000)

print("client / worker ID ",c_ID)

context = zmq.Context()
consumer_RX = context.socket(zmq.PULL)
consumer_RX.connect("tcp://127.0.0.1:5556")
#########

consumer_TX = context.socket(zmq.PUSH)
consumer_TX.connect("tcp://127.0.0.1:5557")

while True:
    work=consumer_RX.recv_json() # TODO: PEP8
    print("from producer ",work) # TODO: PEP8
    data = work['num']
    result = {'consumer':c_ID,'num':data} # TODO: PEP8
    print(result)
#    if data==0:
    consumer_TX.send_json(result)
    print(result)
    time.sleep(1)
