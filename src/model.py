"""
    Defines a Lesson and its parts
    Written By: Kathryn Lecha
    Edit Date: 2021-02-18
"""

from minecraft_learns import Data


from ..errors import ModelNotFound, IncorrectFlow

from minecraft_learns.models import PLSRegressor, LinearRegression, LDA
from minecraft_learns.models import RandomForestClassifier, KNN, KMeans
from minecraft_learns.models import RandomForestRegressor
from minecraft_learns.models import DecisionTreeClassifier
from minecraft_learns.models import DecisionTreeRegression

from sklearn.exceptions import NotFittedError


MODELMAP = {
    "knn": KNN(),
    "lda": LDA(),
    "kmeans": KMeans(),
    "PLS": PLSRegressor(),
    "decision_tree_regression": DecisionTreeRegression(),
    "decision_tree_classification": DecisionTreeClassifier(),
    "linear_regression": LinearRegression(),
    "random_forest_regression": RandomForestRegressor(),
    "random_forest_classification": RandomForestClassifier(),
}


class Model:
    """
    Generic Abstract Lesson Class all lessons inherit from
    """

    def __init__(self):
        self.model = None

    def pick_model(self, model_name):
        """
        set the model to the chosen name
        ---
        @param model_name: string name
        """
        # check if the model can be used in this case
        self._validate_modelname(model_name)

        # set the model to the selected choice
        self.model = MODELMAP[model_name]

    def _validate_modelname(self, model_name):
        """
        Check to see if the provided model name is valid
        ---
        @param model_name: string name of the model
        """
        if model_name not in MODELMAP.keys():
            raise ModelNotFound(model_name)
        return True

    def _set_model(self, model):
        """
        Set the model to the input model_name
        ---
        @param model: model object to use for classification
        """
        self.model = model

    def set_parameters(self, parameters):
        self.model.set_parameters(parameters)

    def _read_data(self, location):
        """
        read in the data selected as a dataframe
        """
        self.data = Data(location)
        return self.data.df

    def process_data(self, location, y_cols, drop_cols):
        """
        Read in the data and save the X and y for prediction
        """
        if self.model is None:
            raise IncorrectFlow("process_data", "Model must be selected first")

        # format X and y
        df = self.read_data(location)

        X = df.drop(drop_cols, axis=1)
        y = df[y_cols]

        self.model.process_data(X, y)

    def train_model(self):
        """
        Train the model for response
        """
        try:
            self.model.train()
        except (NameError):
            raise IncorrectFlow("train_model", "data has not been processed")

    def predict(self, X=None):
        """
        Predict a response on the input data and return response.
        If no data is input, predict on the training data
        ---
        @param X: a numpy array with n predictor observations OR None
        """
        try:
            if X is None:
                return self.model.predict(self.model.X)
            else:
                return self.model.predict(X)
        except NotFittedError:
            raise IncorrectFlow("predict", "Model has not been trained")

    def game_response(self, prediction):
        """
        Trigger Some response in the game
        ---
        returns a message for default event "Say Hello"
        """
        response = {"prediction": prediction, "error": self.model.evaluate()}
        return response
