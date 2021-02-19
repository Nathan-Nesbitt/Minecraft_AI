import json
import asyncio
import websockets

from minecraft_store import Minecraft_Store
from model import Model

"""
    This is the broker file which handles communication between the client and the backend.
    It manages json objects send from the client side and redirects them to the appropriate libraries.

    This file was developed by: Carlos Rueda Carrasco and Nathan Nesbitt
    Date: 30-01-2021
"""


class Broker:
    def __init__(self):
        # Store of the models
        self.models = {}
        self.storage = Minecraft_Store()
        # Starts the connection and the command handling commences
        self.establish_connection()

    def establish_connection(self):
        """
        Starts the connection through a specific port.
        """
        start_connection = websockets.serve(self.response, host="localhost", port=5678)
        asyncio.get_event_loop().run_until_complete(start_connection)
        asyncio.get_event_loop().run_forever()

    async def response(self, websocket, path):
        """
        Listens in for the clients response and loads the json string into a dictionary format.
        Takes the message into another method for handling while returning a message to the client.

        @param  websocket: An initialized websocket that handles messages being sent over
        @param path: Path of the request
        """
        while True:
            try:
                message = await websocket.recv()
                json_dict = json.loads(message)
                print(json_dict)
                status = self.targetProcessId(json_dict)
                for_client = self.message_sent_back(json_dict, status)
                await websocket.send(for_client)
            except websockets.exceptions.ConnectionClosedOK:
                print("Successfully closed!")
                await websocket.close()
                break

    def targetProcessId(self, json_dictionary):
        """
        Handles and checks within the dictionary where the game data needs to be sent, either for storage or for making ML models.

        @param json_dictionary: The json object that was converted into a dictionary
        """
        if json_dictionary["header"]["targetProcess"] == "MinecraftStore":
            return self.store(json_dictionary)
        elif json_dictionary["header"]["targetProcess"] == "MinecraftLearns":
            return self.minecraft_learns(json_dictionary)
        else:
            print("Incorrect naming for targetProcess")
            return False

    def message_sent_back(self, json_dictionary, status):
        """
        Handles the message that is being sent back to the front end so it knows if it was successfully handled or not.

        @param json_dictionary: The json object that was converted into a dictionary
        @param status: True or False depending if the action failed
        """
        message_for_client = {
            "header": {"UUID": json_dictionary["header"]["UUID"], "status": str(status)}
        }
        message_for_client = json.dumps(message_for_client)
        return message_for_client

    def store(self, json_dictionary):
        """
        Stores the game data into the clients local computer.

        @param json_dictionary: The json object that was converted into a dictionary
        """
        file_name = json_dictionary["header"]["fileName"]
        UUID = json_dictionary["header"]["UUID"]
        body = json_dictionary["body"]["data"]["body"]

        # If the UUID hasn't been created, then we need to create a file
        if not UUID in self.storage.files:
            self.storage.add_file(file_name, UUID)

        # Adds the line to the file for this UUID
        try:
            file_location = self.storage.store_filesystem(body, file_name, UUID)
            print(file_location)
            print("Sent to storage")
            return True
        except Exception as e:
            print("Failed to store")
            print(e)
            return False

    def minecraft_learns(self, json_dictionary):
        """
        Calls on the AI to produce ML models.

        @param json_dictionary: The json object that was converted into a dictionary
        """
        try:
            file_name = json_dictionary["header"]["fileName"]
            UUID = json_dictionary["header"]["UUID"]
            model_type = json_dictionary["header"]["model_type"]
            response_variables = json_dictionary["header"]["response_variables"]
            drop_cols - json_dictionary["header"]["drop_cols"]
            function = json_dictionary["header"]["function"]
            #parameters = json_dictionary["header"]["parameters"]

        # Checks the UUID to see if the model exists, if not add it to the dictionary
        if not UUID in self.models:
            add_model(model, UUID)
            # Handles the message being received by the front end
            if function == "process":
                models[UUID].pick_model(model_type, parameters)
                models[UUID].process_data(file_name, response_variable, drop_cols, True)
            elif function == "train":
                models[UUID].train_model()
            elif function == "predict":
                models[UUID].predict()

            print("Sent to Minecraft Learns")
            return True
        except Exception as e:
            print("Failed to send to Minecraft_Learns")
            print(str(e))
            return False

    def add_model(self, model, UUID):
        """
        Adds a new model to the dictionary of models based on the UUID
        sent from the user.

        @param model: Model object that is being added to the list of models
        @param UUID: Callback to the process that initialized the file.
        """
        self.models[UUID] = Model(model = model)

Broker()