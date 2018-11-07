import sys
import zmq
import uuid
import json
import random
import time


port_RX = '5556'  
port_TX = '5557'  

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
    print(f(work['data a'],work['data b']))
    a,b=(work['data a'],work['data b'])
    work.pop('data a')
    work.pop('data b')
    work['data']=f(a,b)
    

   
    
    #data = work['num']
    #result = {'consumer':c_ID,'num':data} # TODO: PEP8
    #print(result)
#    if data==0:
    consumer_TX.send_json(work)
    print('send to collector  ',work)
    time.sleep(1)
