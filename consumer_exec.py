import sys
import zmq
import uuid
import json
import random
import time

######  ZMQ
context = zmq.Context()
consumer_RX = context.socket(zmq.PULL)
consumer_RX.connect("tcp://127.0.0.1:5556")
#########

consumer_TX = context.socket(zmq.PUSH)
consumer_TX.connect("tcp://127.0.0.1:5557")
#############

while True:
    work = consumer_RX.recv_json() 
    print("from producer ",work) 
    exec(work['function'])
   
    dct = dict()
    dct['ID'] = work['ID']
    dct['result'] = f(work['data'])   
    time.sleep(random.randrange(1, 5))
    
    consumer_TX.send_json(dct)
    print('send to collector  ',dct)
   
