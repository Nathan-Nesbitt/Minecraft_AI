"""
Model class for lessons that are regression problems. Sets the model to a
regression model or raises an error

Written By: Kathryn Lecha
Edit Date: 2021-02-14
"""

from ...models.linear_regression import LinearRegression
from ...models.random_forest_regression import RandomForestRegressor

from ...errors import InvalidModelUse
from .lesson import Lesson

from uuid import uuid4

MODELMAP = {
    "linreg": LinearRegression(pca=False),
    "pls": LinearRegression(),
    "random_forest_reg": RandomForestRegressor()
}

class RegressionLesson(Lesson):
    """
    Template Lesson for any classification problem
    """
    def __init__(self, uuid=str(uuid4())):
        super().__init__(uuid)
        self.lessonName = "regression"

    def set_model(self, model_name):
        """
        set the model according to the corresponding model name
        ---
        @param model_name: string name of the model to use
        ---
        raises InvalidModelUse if model_name is incorrect
        """
        # if the model cannot be used here, raise Exception
        if not model_name in MODELMAP.keys():
            raise InvalidModelUse(model_name)

        # otherwise set the corresponding model
        super().set_model(MODELMAP[model_name])