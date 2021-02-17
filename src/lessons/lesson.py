"""
    Defines a Lesson and its parts

    Written By: Kathryn Lecha
    Edit Date: 2021-02-14
"""

from minecraft_learns import Data
from ..errors import InvalidDataUse, ModelNotFound


VALIDNAMES = [
    "PLS", "decision_tree", "random_forest_regression",
    "random_forest_classification", "lda", "kmeans", "knn", "linear_regression"
    ]


class Lesson:
    """
    Generic Abstract Lesson Class all lessons inherit from
    """
    def __init__(self):
        self.model = None

    def read_data(self, location):
        """
        read in the data selected as a dataframe
        """
        self.data = Data(location)
        return self.data.df

    def validate_modelname(self, model_name):
        """
        Check to see if the provided model name is valid
        ---
        @param model_name: string name of the model
        """
        if model_name not in VALIDNAMES:
            raise ModelNotFound(model_name)
        return True

    def set_model(self, model):
        """
        Set the model to the input model_name
        ---
        @param model: model object to use for classification
        """
        self.model = model

    def process_data(self, X, y):
        self.model.process_data(X, y)

    def train_model(self):
        self.model.train()

    def predict(self, X):
        """
        predict for the input X
        ---
        @param X: a dataframe of n response variables and m response
        """
        if (X.columns != self.model.X.columns).any():
            raise InvalidDataUse(X)

        return self.model.predict(X)

    def game_response(self, prediction):
        """
        Trigger Some response in the game
        ---
        returns a message for default event "Say Hello"
        """
        return None
