import zmq
import random
import sys
import time
import uuid

port = "5556"
if len(sys.argv) > 1:
    port =  sys.argv[1]
    int(port)

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:%s" % port)

# function for client to execute
fun_s = '''
def f(a,b):
    # print("Sum of two elements")
    return a+b
'''
fun_topic = 10000
data_topic = 10001

string = str('test') # TODO: no need to convert a string to a string
# generate topic and masage randomly
while True:
    topic = random.randrange(9999,10005) # TODO: PEP8
    messagedata = random.randrange(10,200) # TODO: PEP8

    a=random.randrange(10,200) # TODO: PEP8
    b=random.randrange(10,200) # TODO: PEP8
    data_s = b"%d,%d" % (a,b)
    socket.send(b'%d %s'%(data_topic, data_s)) # TODO: PEP8
    socket.send(b'%d %s'%(fun_topic, bytes(fun_s,'utf-8'))) # TODO: PEP8

    print("data: ", a, b)
    print("funciont to TX: ", fun_s)

    time.sleep(1)
