import websockets
import json
import asyncio

"""
This file was developed by Carlos
"""
# Testing class to mimic client sending message
# Run client.py again but switching targetProcess = Storage for different result

async def send_message():
    async with websockets.connect("ws://localhost:5678") as socket:
        message = {
	                    "header": {
		                    "targetProcess": "MinecraftLearns",
		                    "fileName": "MyData"
	                    },
	                    "body": {
		                    "biome": "desert",
		                    "version": 1
	                    }
                    }
        message_string = json.dumps(message)
        await socket.send(message_string)
        print(await socket.recv())
asyncio.get_event_loop().run_until_complete(send_message())