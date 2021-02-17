"""
    Defines a Lesson and its parts
    
    Written By: Kathryn Lecha
    Edit Date: 2021-02-14
"""

from ..data import Data
from ..errors import InvalidDataUse

from uuid import uuid4

states = ["no data", "no model", "no X/y", "untrained"]


class Lesson:
    """
    Generic Abstract Lesson Class all lessons inherit from
    """
    def __init__(self, uuid=str(uuid4())):
        self.uuid = uuid
        self.lessonName = "generic"
        self.model = None
        self.state = "no model"

    def read_data(self, location):
        """
        read in the data selected as a dataframe
        """
        self.data = Data(location)
        return self.data.df
    
    def set_model(self, model):
        """
        Set the model to the input model_name
        ---
        @param model: model object to use for classification
        """
        self.model = model

    def set_X(self, X):
        """
        Set the training X data
        ----
        @param X: 
        """
        self.X = X

    def set_y(self, y_column):
        """
        Set the training y data
        ----
        @param y_column: string column name for response variable
        """
        self.y = self.data.df[y_column]

    def set_X_y(self, X_columns, y_column):
        """
        Set the training X and y data
        ----
        @param X_columns: list of column names for predictor variables
        @param y_column: string column name for response variable
        """
        self.set_X(X_columns)
        self.set_y(y_column)
    
    def process_data(self):
        self.model.process_data(self.X, self.y)

    def train_model(self):
        self.model.train()

    def predict(self, X):
        """
        predict for the input X
        ---
        @param X: a dataframe of n response variables and m response
        """
        if X.columns != self.X.columns:
            raise InvalidDataUse(X)

        return self.model.predict(X)
    
    def game_response(self, prediction):
        """
        Trigger Some response in the game
        ---
        returns a message for default event "Say Hello"
        """
        message = {
            "header": {
                "UUID": self.uuid,
                "targetProcess": "MinecraftAI",
                "lessonName": self.lessonName
            },
            "body": {
                "response": {
                    "actor": "bot",
                    "command": "Say",
                    "arg": "\"Hello\""
                }
            }
        }
        return message
    
