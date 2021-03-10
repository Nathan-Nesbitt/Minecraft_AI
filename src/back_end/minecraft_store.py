"""
    This is a class that helps store data into a local location on the clients computer.

    Written By: Carlos Rueda Carrasco and Nathan Nesbitt
    Date: 2021-01-08
"""
# Import all the necessary packages
import json
from datetime import datetime
from .data import Data


class Minecraft_Store:
    def __init__(self):
        # Files that can be written to
        self.files = {}

    def store_filesystem(self, data, name, file):
        """
        Method that takes the data from the client and then stores it into the local computer.

        @param data: The data being stored, will be in a json dictionary format

        @param name: The name of the file being used

        @param file: Which file you are writing the data to, the UUID is normally this
        """
        self.files[file].save_observation(data)
        return str(self.files[file].absolute_path())

    def add_file(self, filename, UUID):
        """
        Adds a new file to the Minecraft_Store object based on the UUID
        sent from the user. This allows for multiple files and multiple
        event handlers to be run at the same time.

        @param filename: Filename where the data should be saved.
        @param UUID: Callback to the process that initialized the file.
        """
        self.files[UUID] = Data(filename=filename)