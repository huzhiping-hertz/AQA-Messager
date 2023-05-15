#!/usr/bin/env python3

import asyncio
import websockets
import time
from WebApi import WebApi

async def RequestHandler(websocket):
    print("newc:connection and waiting parameters....")
    
    parameters = await websocket.recv()
    print("recv:"+parameters)
    
    try:
        while True:
            # msg="{'tid':1,'lostpacket':0.2,'delay':'2mm','jitter':1,'mos':1}"
            # await websocket.send(msg)
           
            api=WebApi()
            await websocket.send(api.getLostPacket())
            await websocket.send(api.getJitter())
            await websocket.send(api.getDelay())
            time.sleep(3)
    finally:
        websocket.close()
        
async def main():
    async with websockets.serve(RequestHandler, "localhost", 8000):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())