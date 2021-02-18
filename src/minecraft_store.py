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
    def __init__(self): 
        self.client_data = Data()

    def store_filesystem(self, data, name):
        """
            Method that takes the data from the client and then stores it into the local computer.

            @param data: The data being stored, will be in a json dictionary format
        """
        if (self.client_data.already_made(name)==True):
            self.client_data.add_observation(data)
        else:
            self.client_data.save_observation(data)
            self.client_data.rename_file(name)
        return str(self.client_data.absolute_path())

    def timestamp_format(self):
        """
            Method that retrieves the time and date for our file naming
        """
        time_sent_back = ""
        current = datetime.now().strftime("%Y-%m-%d")
        time_sent_back = time_sent_back + current
        return time_sent_back