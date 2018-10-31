
import zmq
import random
import sys
import time
import uuid

port = "5556"


context = zmq.Context()
socket = context.socket(zmq.PUSH)
socket.bind("tcp://127.0.0.1:5556")


while True:
    work_msg = {'num':12345}
    
    socket.send_json(work_msg)
    
    print(" to send ", work_msg)
    time.sleep(1)


    
    
