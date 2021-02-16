"""
    This is the Data class for minecraft-api. This creates an object for a file
    where data can be stored. It opens it for as long as the object exists so
    that the user doesn't have to optimize anything and can simply tell the
    computer to save the data.

    Collaborators: Nathan Nesbitt, Carlos Rueda, Kathryn Lecha
    Modified: 2021-01-31
"""

import uuid
import os

from datetime import datetime
from json import loads
from pandas import concat, DataFrame, Series


INVALID_PROPS = [
    "AccountType", "AcquisitionMethodID", "ActiveSessionID", "AppSessionID",
    "AuxType", "Build", "BuildNum", "BuildPlat", "Cheevos", "ClientId",
    "CurrentInput", "CurrentNumDevices", "DeviceSessionId",
    "GlobalMultiplayerCorrelationId", "NetworkType", "Plat", "Treatments",
    "UserId", "WorldSessionId", "isTrial", "locale", "vrMode", "Branch",
    "BuildTypeID", "Commit", "SchemaCommitHash"
]



class Data:

    def __init__(self, location="", filename=str(uuid.uuid4())):
        """
            Initializes an object that is an open file that can be written to.

            @param location: String path to a directory on the system that the
                user can access
            @param filename: String filename that the user can access.
        """
        self.location = location
        self.filename = filename + ".csv"
        self.data = []

    def save_data(self):
        """
            Save the dataframe as a csv at the saved filepath
            ---
            outputs the absolute path of the file
        """
        DataFrame(self.data).to_csv(self.location + self.filename, index=False)
        return self.absolute_path()
    
    def save_observation(self, data_json):
        """
            save the new observation
            ---
            @param data_json: a json of a single event response
        """
        self.add_observation(data_json)
        self.save_data()

    def add_observation_list(self, data_list):
        """
            save a series of events to the dataframe
        """
        self.data.extend(data_list)

    def add_observation(self, data_json):
        """
            append an observation to the list
            ---
            @param data_json: a json of a single event response
        """
        data_json = self._format_event_dict(data_json)
        self.data.append(data_json)

    def delete_data(self):
        """ Deletes the data """
        os.remove(self.location + self.filename)
        try:
            os.rmdir(self.location)
        except PermissionError:
            pass
        except OSError:
            pass

    def absolute_path(self):
        absolute_location = os.path.abspath(self.location+self.filename)
        return str(absolute_location)

    def _format_event_dict(self, data_json):
        """
            Format an data json as a row in a csv
            ---
            @param event: an event in json format. each event has an
            "eventName", a dictionary of "measurements" and a dictionary of
            "properties"
            ---
            outputs a formatted dictionary
        """
        # ensure that the event is a dictionary
        if isinstance(data_json, str):
            data_json = loads(data_json)
        new_data = {}
        
        # save the data values
        new_data["eventName"] = data_json["eventName"]
        new_data["triggerTime"] = datetime.now()

        for dict_key in data_json["measurements"].keys():
            new_data[dict_key] = data_json["measurements"][dict_key]

        for dict_key in data_json["properties"].keys():
            # only save valid properties
            if not dict_key in INVALID_PROPS:
                new_data[dict_key] = data_json["properties"][dict_key]

        return new_data
