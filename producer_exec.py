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
    a = random.randrange(1,100)
    b = random.randrange(1,100)
    c = random.randrange(1,100)
    d = random.randrange(1,100)
    work_msg = {
        'ID': msg_ID,
        'code' : [1,0],
        'function': fun,
        'data':{
            'a': a,
            'b': b,
        },
    }
    socket.send_json(work_msg)

    work_msg = {
        'ID': msg_ID,
        'code' : [1,1],
        'function': fun,
        'data':{
            'a': a+c,
            'b': b+d,
        },
    }
    socket.send_json(work_msg)
    
    work_msg = {
        'ID': msg_ID,
        'code' : [0,1],
        'function': fun,
        'data':{
            'a': c,
            'b': d,
        },
    }
    socket.send_json(work_msg)
    
    print(work_msg)
    socket.send_json(work_msg)
    time.sleep(10) 
