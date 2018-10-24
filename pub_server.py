
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

while True:
    topic = random.randrange(9999,10005)
    messagedata = random.randrange(1,215)
    print("%d %d" % (topic, messagedata))
    socket.send(b"%d %d" % (topic, messagedata))
    time.sleep(1)
