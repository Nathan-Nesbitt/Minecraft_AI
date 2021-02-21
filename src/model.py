"""
    Defines a Lesson and its parts
    Written By: Kathryn Lecha
    Edit Date: 2021-02-19
"""

from errors import ModelNotFound

from minecraft_learns import Data, IncorrectFlow, label_encoding, encode_labels
from minecraft_learns.models import PLSRegressor, LinearRegression, LDA
from minecraft_learns.models import RandomForestClassifier, KNN, KMeans
from minecraft_learns.models import RandomForestRegressor
from minecraft_learns.models import DecisionTreeClassifier
from minecraft_learns.models import DecisionTreeRegression


MODELMAP = {
    "knn": KNN,
    "lda": LDA,
    "kmeans": KMeans,
    "PLS": PLSRegressor,
    "decision_tree_regression": DecisionTreeRegression,
    "decision_tree_classification": DecisionTreeClassifier,
    "linear_regression": LinearRegression,
    "random_forest_regression": RandomForestRegressor,
    "random_forest_classification": RandomForestClassifier,
}


class Model:
    """
    Generic Abstract Lesson Class all lessons inherit from
    """

    def __init__(self, model=None):
        self.model = model

    def pick_model(self, model_name, params={}):
        """
        set the model to the chosen name
        ---
        @param model_name: string name
        @param params: dictionary of parameters to set
        """
        # check if the model can be used in this case
        self._validate_modelname(model_name)

        # set the model to the selected choice
        self.model = MODELMAP[model_name]()
        self.model.set_parameters(params)

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
        """
        set the parameters of the model
        ---
        @param params: dictionary of parameters to set
        """
        if parameters is not None:
            self.model.set_parameters(parameters)

    def _read_data(self, location):
        """
        read in the data selected as a dataframe
        """
        return Data(location).get_data()

    def process_data(self, location, y_cols, feature_cols, drop=False):
        """
        Read in the data and save the X and y for prediction
        """
        if self.model is None:
            raise IncorrectFlow("process_data", "Model must be selected first")

        df = self._read_data(location)

        # format X and y
        y = df[y_cols]
        X = self._encode_labels(self._get_features(df, feature_cols, drop))

        self.model.process_data(X, y)

    def _get_features(self, data, feature_cols, drop=False):
        """
        get the predictor/feature variables from the data
        ---
        @param data: a 2D data matrix of n observations and m predictors
        @param interaction_cols: list of columns to interact
        """
        if drop:
            return data.drop(feature_cols, axis=1)
        else:
            return data[feature_cols]

    def _encode_labels(self, data):
        """
        encode the labels in the data and save the encoder
        ---
        @param data: a 2D data matrix of n observations and m predictors
        """
        if "object" in data.dtypes.values:
            self.label_encoder, data = label_encoding(data)
            return data
        else:
            return data

    def train_model(self):
        """
        Train the model for response
        """
        try:
            self.model.train()
        except (NameError):
            raise IncorrectFlow("train_model", "data has not been processed")

    def predict(self, test_X=None):
        """
        Predict a response on the input data and return response.
        If no data is input, predict on the training data
        ---
        @param test_X: a numpy array with n predictor observations OR None
        """
        if test_X is None:
            return self.model.predict(self.model.X)
        else:
            if hasattr(self, "label_encoder"):
                test_X = encode_labels(self.label_encoder, test_X)
            return self.model.predict(test_X)

    def game_response(self, prediction):
        """
        Trigger Some response in the game
        ---
        returns a message for default event "Say Hello"
        """
        response = {"prediction": prediction.tolist(), "error": self.model.evaluate()}
        return response
