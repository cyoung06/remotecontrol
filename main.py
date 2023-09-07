import json
import sys

from arduino_serial import MovingPlatform

import asyncio
import websockets

platform = MovingPlatform(sys.argv[1])


async def handler(websocket, path):
    data = await websocket.recv()
    a = json.loads(data)

    platform.go([a["x"], a["y"]], a["rot"])

    await websocket.send(json.dumps({"status": "good"}))


start_server = websockets.serve(handler, "localhost", 8000)

asyncio.get_event_loop().run_until_complete(start_server)

asyncio.get_event_loop().run_forever()
