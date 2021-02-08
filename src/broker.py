import json
import asyncio
import websockets
#from Minecraft_Store import Minecraft_Store
"""
    This is the broker file which handles communication between the client and the backend.
    It manages json objects send from the client side and redirects them to the appropriate libraries.

    This file was developed by: Carlos Rueda Carrasco and Nathan Nesbitt
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
    while True:
        message = await websocket.recv()
        json_dict = json.loads(message)
        status = targetProcessId(json_dict)
        for_client = message_sent_back(json_dict, status)
        await websocket.send(for_client)
    #websocket.close()

def targetProcessId(json_dictionary):
    """
        Handles and checks within the dictionary where the game data needs to be sent, either for storage or for making ML models.

        @param json_dictionary: The json object that was converted into a dictionary
    """
    if (json_dictionary['header']['targetProcess']=='MinecraftStore'):
        return store(json_dictionary)
    elif(json_dictionary['header']['targetProcess']=='MinecraftLearns'):
        return minecraft_learns(json_dictionary)
    else:
        print("Incorrect naming for targetProcess")
        return False

def message_sent_back(json_dictionary, status):
    """
        Handles the message that is being sent back to the front end so it knows if it was successfully handled or not. 

        @param json_dictionary: The json object that was converted into a dictionary
        @param status: True or False depending if the action failed
    """
    message_for_client = {
                            "header": {
                                "UUID": json_dictionary['header']['UUID'],
                                "status": str(status)
                            }
                        }
    message_for_client = json.dumps(message_for_client)
    return message_for_client

def store(json_dictionary):
    """
        Stores the game data into the clients local computer.

        @param json_dictionary: The json object that was converted into a dictionary
    """
    try:
        file_name = json_dictionary['header']['fileName']
        #storage = Minecraft_Store()
        #file_location = storage.store_filesystem(json_dictionary, file_name)
        #file_list[file_name] = file_location
        print("Sent to storage")
        return True
    except Exception:
        print("Failed to store")
        return False

def minecraft_learns(json_dictionary):
    """
        Calls on the AI to produce ML models.

        @param json_dictionary: The json object that was converted into a dictionary
    """
    try:
        print("Sent to Minecraft Learns")
        return True
    except Exception:
        print("Failed to send to Minecraft_Learns")
        return False

# Starts the connection and the command handling commences
establish_connection()