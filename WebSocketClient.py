#!/usr/bin/env python3

import asyncio
from websockets.sync.client import connect

def DataRequest():
    uri = "ws://localhost:8000"
    with connect(uri) as websocket:
    
        parameters = "{'tid':1,'timespan':'20m','src':'172.25.65.38','dst':'172.25.65.239'}"
        websocket.send(parameters)
        print("send:"+parameters)

        try:
            while True:
                response = websocket.recv()
                print("recv:"+response)
        except:
            print ("Some Error")
        finally:
            websocket.close()

if __name__ == "__main__":
    DataRequest()