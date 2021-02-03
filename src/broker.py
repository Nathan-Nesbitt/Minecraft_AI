import json
import asyncio
import websockets
"""
    This is the broker file which handles communication between the client and the backend.
    It manages json objects send from the client side and redirects them to the appropriate libraries.

    This file was developed by: Carlos Rueda Carrasco
    Date: 30-01-2021
"""

file_list = {}

def establish_connection():
    """
        Starts the connection through a specific port.
    """
    start_connection = websockets.serve(response, host='localhost', port=5678)
    asyncio.get_event_loop().run_until_complete(start_connection)
    asyncio.get_event_loop().run_forever()

async def response(websocket, path):
    """
        Listens in for the clients response and loads the json string into a dictionary format.
        Takes the message into another method for handling while returning a message to the client.

        @param  websocket: An initialized websocket that handles messages being sent over
        @param path: Path of the request
    """
    message = await websocket.recv()
    json_dict = json.loads(message)
    targetProcessId(json_dict)
    await websocket.send("Message received")

def targetProcessId(json_dictionary):
    """
        Handles and checks within the dictionary where the game data needs to be sent, either for storage or for making ML models.

        @param json_dictionary: The json object that was converted into a dictionary
    """
    if (json_dictionary['header']['targetProcess']=='Storage'):
        store(json_dictionary)
    elif(json_dictionary['header']['targetProcess']=='MinecraftLearns'):
        minecraft_learns(json_dictionary)
    else:
        print("Incorrect naming for targetProcess")

def store(json_dictionary):
    """
        Stores the game data into the clients local computer.

        @param json_dictionary: The json object that was converted into a dictionary
    """
    file_name = json_dictionary['header']['fileName']
    print("Sent to storage")

def minecraft_learns(json_dictionary):
    """
        Calls on the AI to produce ML models.

        @param json_dictionary: The json object that was converted into a dictionary
    """
    print("Sent to Minecraft Learns")

# Starts the connection and the command handling commences
establish_connection()