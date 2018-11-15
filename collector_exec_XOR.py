import sys
import zmq
import uuid
import json
import pprint
import time


######  ZMQ
context = zmq.Context()
collector_RX = context.socket(zmq.PULL)

collector_RX.bind("tcp://127.0.0.1:5557")
collector_data = {}
#########

active_tasks = dict()
completed_tasks = set()


while True:
    rx = collector_RX.recv_json()
    _id = rx['ID']
    if _id in completed_tasks:
        continue
    
    
    if _id not in active_tasks:
        active_tasks[_id] = list()

    active_tasks[_id].append(rx)

    if len(active_tasks[_id])==2:
        print(active_tasks[_id])
        completed_tasks.add(_id)
        #del active_tasks[_id]
        if active_tasks[_id][0]['code'] == [1,1] or active_tasks[_id][1]['code'] == [1,1]:
            if active_tasks[_id][0]['code']==[1,1]:
                if active_tasks[_id][1]['code']==[0,1]:
                    print('sum of c+d = ', active_tasks[_id][0]['result']-active_tasks[_id][1]['result'])
                else: print('sum of a+b = ', active_tasks[_id][0]['result']-active_tasks[_id][1]['result'])
            if active_tasks[_id][1]['code']==[1,1]:
                if active_tasks[_id][0]['code']==[0,1]:
                    print('sum of a+b = ', active_tasks[_id][1]['result']-active_tasks[_id][0]['result'])
                else: print('sum of c+d = ', active_tasks[_id][1]['result']-active_tasks[_id][0]['result'])
        else:
            print("test")
        del active_tasks[_id]        
        
    
        
             
    #print(RX_msg)
    #id = rx['ID']

    #peeling decoder
    
