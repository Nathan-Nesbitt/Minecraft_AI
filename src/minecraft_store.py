"""
    This is a class that helps store data into a local location on the clients computer.

    Written By: Carlos Rueda Carrasco
    Date: 2021-01-08
"""
# Import all the necessary packages
import json
from datetime import datetime
from data import Data

class Minecraft_Store:
    def __init__(self, name): 
        time = str(self.timestamp_format())
        self.client_data = Data(filename=name + time)

    def store_filesystem(self, data, name):
        """
            Method that takes the data from the client and then stores it into the local computer.

            @param data: The data being stored, will be in a json dictionary format
        """
        self.client_data.rename_file(name)
        self.client_data.save_observation(data)
        return str(self.client_data.absolute_path())

    def timestamp_format(self):
        """
            Method that retrieves the time and date for our file naming
        """
        time_sent_back = ""
        current = datetime.now().strftime("%Y-%m-%d")
        time_sent_back = time_sent_back + current
        return time_sent_back