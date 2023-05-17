#!/usr/bin/env python3

import asyncio
import websockets
import time
import json
from threading import Thread
from WebApi import WebApi

async def handler(ws):

    while True:
        params=await ws.recv()
        paramObj=json.loads(params)
        asyncio.create_task( process(ws,paramObj))
    
    
async def process(ws,paramObj):

    api=WebApi()
    try:
        while True:
            rsObj={"packet_lost":[],"delay":[],"jitter":[]}
            for idx,item in enumerate(paramObj):
                src=item["src"]
                dst=item["dst"]
                rsObj["packet_lost"].append(api.getLostPacket(src,dst))
                rsObj["delay"].append(api.getDelay(src,dst))
                rsObj["jitter"].append(api.getJitter(src,dst))
            print(json.dumps(rsObj))
            await ws.send(json.dumps(rsObj)) 
            await asyncio.sleep(3)
    finally:
        ws.close()
 
async def reqeust(ws):
    parameters = await ws.recv()
    print("recv:"+parameters)
    paramObjs=json.loads(parameters)
    
      
async def main():
    async with websockets.serve(handler, "0.0.0.0", 8000):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())