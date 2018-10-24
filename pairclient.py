import zmq
import random
import sys
import time

port = "5556"
context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.connect("tcp://localhost:5556")

while True:
    msg = socket.recv()
    print(msg)
    socket.send(b"client message to server1")
    time.sleep(1)
