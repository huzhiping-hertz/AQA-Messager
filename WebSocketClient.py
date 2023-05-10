#!/usr/bin/env python3

import asyncio
import websockets

async def DataRequest():
    uri = "ws://localhost:8000"
    async with websockets.connect(uri) as websocket:
        
        parameters = "{'tid':1,'timespan':'20m','src':'172.25.65.38','dst':'172.25.65.239'}"
        await websocket.send(parameters)
        print("send:"+parameters)

        try:
            while True:
                response = await websocket.recv()
                print("recv:"+response)
        finally:
            websocket.close()

if __name__ == "__main__":
    asyncio.run(DataRequest())