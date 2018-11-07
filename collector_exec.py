import sys
import zmq
import uuid
import json
import pprint
import time


port_RX = '5557'  # port PULL


######  ZMQ
# Socket to talk to server


context = zmq.Context()
collector_RX = context.socket(zmq.PULL)

collector_RX.bind("tcp://127.0.0.1:5557")
collector_data = {}
#########

for x in range (1000): # TODO: PEP8
    RX_msg = collector_RX.recv_json() # TODO: use a better name, 
    print(RX_msg)

    #if collector_data.get(RX_msg['ID']):
     #   collector_data[collector['consumer']] += 1
    #else:
     #   collector_data[collector['consumer']] = 1
    #if x==99: # TODO: PEP8
     #   pprint.pprint(collector_data)
    #print(collector_data)

   # time.sleep(1)
