import websockets
import json
import asyncio

"""
	Testing file to mimic client sending message.
	Run client.py again but switching targetProcess = Storage for different result
	
	This file was developed by: Carlos Rueda Carrasco
    Date: 30-01-2021
"""

async def send_message():
    async with websockets.connect("ws://localhost:5678") as socket:
        message = {
	                    "header": {
		                    "targetProcess": "MinecraftLearns",
		                    "fileName": "MyData",
							"modelFunction": "Linear Regression"
	                    },
	                    "body": {
		                    "data": {

							}
	                    }
                    }
        message_string = json.dumps(message)
        await socket.send(message_string)
        print(await socket.recv())
asyncio.get_event_loop().run_until_complete(send_message())