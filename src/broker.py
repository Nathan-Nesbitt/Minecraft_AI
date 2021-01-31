import json
import asyncio
import websockets
"""
This file was developed by Carlos
"""
file_list = []

def establish_connection():
    start_connection = websockets.serve(response, host='localhost', port=5678)
    asyncio.get_event_loop().run_until_complete(start_connection)
    asyncio.get_event_loop().run_forever()

async def response(websocket, path):
    message = await websocket.recv()
    json_dict = json.loads(message)
    targetProcessId(json_dict)
    await websocket.send("Message received")

def targetProcessId(json_dictionary):
    if (json_dictionary['header']['targetProcess']=='Storage'):
        store(json_dictionary)
    elif(json_dictionary['header']['targetProcess']=='MinecraftLearns'):
        minecraft_learns(json_dictionary)
    else:
        print("Incorrect naming for targetProcess")

def store(json_dictionary):
    file_name = json_dictionary['header']['fileName']
    print("Sent to storage")

def minecraft_learns(json_dictionary):
    print("Sent to Minecraft Learns")

establish_connection()