import zmq
import time


context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

print("Connecting to hello world server…")

#  Do 10 requests, waiting each time for a response
for request in range(10):
    print("Sending request %s …" % request)
    socket.send(b"Hello")

    #  Get
    message = socket.recv()
    print("Received reply %s [ %s ]" % (request, message))
    time.sleep(0.5)
    
