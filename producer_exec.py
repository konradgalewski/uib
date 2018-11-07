import zmq
import random
import sys
import time
import uuid


context = zmq.Context()
socket = context.socket(zmq.PUSH)
socket.bind("tcp://127.0.0.1:5556")

fun='''
def f(a,b):
    return a+b

'''

while True:
#for _ in range(5):
    msg_ID=str(uuid.uuid4()) #random number random ID
    work_msg = {'ID':msg_ID,'function':fun,'data a':random.randrange(1,1000), 'data b':random.randrange(1,1000)}
    print(work_msg)
    socket.send_json(work_msg)
    #print(" to send ", work_msg)
    time.sleep(random.randrange(1,10)) #simulate of dalay
