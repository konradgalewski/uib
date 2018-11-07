import zmq
import random
import sys
import time
import uuid


context = zmq.Context()
socket = context.socket(zmq.PUSH)
socket.bind("tcp://127.0.0.1:5556")

fun='''
def f(dct):
    return dct['a']+dct['b']
'''

while True:
    msg_ID = str(uuid.uuid4()) #random ID
    work_msg = {
        'ID': msg_ID,
        'function': fun,
        'data':{
            'a': random.randrange(1,100),
            'b': random.randrange(1,100),
        },
    }
    print(work_msg)
    socket.send_json(work_msg)
    time.sleep(1) 
