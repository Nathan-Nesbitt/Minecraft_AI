"""
Predict where to mine for specific materials

Written By: Kathryn Lecha
Edit Date: 2021-02-14
"""

from .lesson import Lesson
from ..errors import InvalidModelUse, IncorrectFlow

from minecraft_learns.models import PLSRegressor
from minecraft_learns.models import RandomForestRegressor
from minecraft_learns.models import LinearRegression

from numpy import power, sqrt
from numpy import sum as np_sum
from sklearn.exceptions import NotFittedError


MODELMAP = {
    "PLS": PLSRegressor(one_hot_encode=["Biome"]),
    "decision_tree": LinearRegression(one_hot_encode=["Biome"]),
    "forest_reg": RandomForestRegressor()
}


def euclidean_distance(a, b):
    """
    find the euclidean distance between a and b
    ---
    @param a: numpy 2D array representing n observations of m predictors
    @param b: numpy array representing one observation with m predictors
    ---
    Formula for Euclidean Distance:
        dist = sqrt(sum((a[1]+b[1])^2 + ... + (a[n]+b[n])^2))
    """
    return sqrt(np_sum(power(a - b, 2), axis=1))


class PredictMineLesson(Lesson):
    """
    Class for predicting where to mine for specific materials
    """
    def __init__(self, material="coal_ore"):
        super().__init__()
        self.material = material

    def automated_execute(self, loc_current, model_name="forest_reg"):
        """
        automatically execute all parts of model training
        ---
        @param loc_current: location of the player in [x, y, z] coordinates
        @param model_name: string name of the model to train
        """
        self.pick_model(model_name)
        self.process_data()
        self.train_model()
        predictions = self.predict()
        return self.game_response(loc_current, predictions)

    def pick_model(self, model_name="forest_reg"):
        """
        set the model to the chosen name
        ---
        @param model_name: string name
        """
        # check if the model can be used in this case
        self.validate_modelname(model_name)

        # set the model to the selected choice
        self.model = MODELMAP[model_name]

    def validate_modelname(self, model_name):
        """
        check if selected model can be used in this
        ---
        @param model_name: string name
        """
        # check to see if model is implemented in Minecraft Learns
        super().validate_modelname(model_name)

        # Check to see if chosen model can be used in this lesson
        if model_name not in MODELMAP.keys():
            raise InvalidModelUse(model_name)

    def load_data(self):
        """
        Read in the data and format it for prediction. Select only datapoints
        related to chosen material
        """
        # read in data
        df = super().read_data("data/block_broken.csv")

        # filter for material and return
        return df[df["Block"] == self.material]

    def process_data(self):
        """
        Read in the data and save the X and y for prediction
        """
        if self.model is None:
            raise IncorrectFlow("process_data", "Model must be selected first")

        # format X and y
        df = self.load_data()
        drop_cols = [
            "FeetPosX", "FeetPosY", "FeetPosZ", "eventName", "Block",
            "PlacementMethod", "triggerTime", "Difficulty", "editionType",
            "Namespace", "PlayerBiome"
        ]
        X = df.drop(drop_cols, axis=1)
        y = df[["FeetPosX", "FeetPosY", "FeetPosZ"]]

        # process the model
        self.model.process_data(X, y)

    def train_model(self):
        """
        Train the model for response
        """
        try:
            self.model.train()
        except(NameError):
            raise IncorrectFlow("train_model", "data has not been processed")

    def predict(self, X=None):
        """
        Predict a response on the input data and return response.
        If no data is input, predict on the training data
        ---
        @param X: a dataframe with n predictor observations OR None
        """
        try:
            if X is None:
                return super().predict(self.model.X)
            else:
                return super().predict(X)
        except(NotFittedError):
            raise IncorrectFlow("predict", "Model has not been trained")

    def find_closest_point(self, loc_current, predictions):
        """
        get the closest location to the current location
        ---
        @param loc_current: location of the player in [x, y, z] coordinates
        @param predictions: dataframe of predictions of [x, y, z] coordinates
        """
        distances = euclidean_distance(loc_current, predictions)
        return predictions[distances == distances.min()][0]

    def get_error(self, y, predicted):
        """
        get error
        ---
        @param y: numpy 2D array true y locations of [x, y, z] coordinates
        @param predictions: numpy 2D array [x, y, z] coordinates
        """
        return euclidean_distance(y, predicted).median()

    def game_response(self, loc_current, predictions):
        """
        select game response
        ---
        @param loc_current: location of the player in [x, y, z] coordinates
        @param predictions: dataframe of predictions of [x, y, z] coordinates
        """
        closest_point = self.find_closest_point(loc_current, predictions)
        error = self.get_error(self.model.y, predictions)

        response = {
            "prediction": {
                "X": closest_point[0],
                "Y": closest_point[1],
                "Z": closest_point[2]
            },
            "error": error,
            "bot-action": "Say"
        }
        return response
