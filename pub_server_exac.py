
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

fun_s = '''
def f(a,b):
    #funcian TX to client and exec.
    #print("Sum of To element")
    return a+b
'''
fun_topic =10000

data_topic= 10001
string = str('test')
# generate topic and masage randomly 
while True:
    topic = random.randrange(9999,10005)
    messagedata = random.randrange(10,200)
    
    a=random.randrange(10,200)
    b=random.randrange(10,200)
    data_s = b"%d,%d" % (a,b)
    socket.send(b'%d %s'%(data_topic, data_s))
    socket.send(b'%d %s'%(fun_topic, bytes(fun_s,'utf-8')))

    print("data: ", a, b)
    print("funciont to TX: ", fun_s)
    
    time.sleep(1)
    
    
