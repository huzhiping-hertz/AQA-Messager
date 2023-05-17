#!/usr/bin/env python3

import asyncio
from websockets.sync.client import connect

def DataRequest():
    uri = "ws://172.25.77.3:8000"
    with connect(uri) as websocket:
    
        parameters = '[{"src":"172.18.15.66","dst":"172.18.15.67"}]'
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