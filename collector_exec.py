import sys
import zmq
import uuid
import json
import pprint
import time


######  ZMQ
context = zmq.Context()
collector_RX = context.socket(zmq.PULL)

collector_RX.bind("tcp://127.0.0.1:5557")
collector_data = {}
#########

while True:
    RX_msg = collector_RX.recv_json()  
    print(RX_msg)

