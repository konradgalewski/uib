import sys
import zmq
import uuid
import json

port = "5556"  # default port
# ext arg for ports
if len(sys.argv) > 1:
    port =  sys.argv[1]
    int(port)

if len(sys.argv) > 2:
    port1 =  sys.argv[2]
    int(port1)
######  ZMQ
# Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)
print("Collecting updates from weather server...")
socket.connect ("tcp://localhost:%s" % port)
#########

if len(sys.argv) > 2:
    socket.connect ("tcp://localhost:%s" % port1)

c_ID=uuid.uuid4()
print("client ID ",c_ID)

i=0 # TODO: unused
socket.setsockopt_string(zmq.SUBSCRIBE,"")
while True:


    data = socket.recv()
    funcion = socket.recv()
    print("what we get ",data,"  ", funcion)

    data=data.decode('utf-8') #decode string use utf-8 # TODO: PEP8
    funcion=funcion.decode('utf-8') #decode string use utf-8  # TODO: PEP8

    x, y = 0, 0
    if data[0:5]=='10001':
        print("data",data)
        topic,data=data.split() #data local
        a,b=data.split(',')  # TODO: PEP8
        x=int(a) # TODO: PEP8
        y=int(b) # TODO: PEP8

    fun_s = None
    if funcion[0:5]=='10000':  # TODO: PEP8
        print("fun",funcion)  # TODO: PEP8
        fun_s=funcion[5:]  # TODO: PEP8
        print("fun_s", fun_s)

    exec(fun_s)  #exec return none no ruturn

    print("exec of funcion TX to client ->for ",x, "and ", y," Sum =", f(x,y))  # TODO: PEP8
