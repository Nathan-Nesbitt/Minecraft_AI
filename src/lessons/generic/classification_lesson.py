"""
Model class for lessons that are classification problems. Sets the model to a
classification model or raises an error

Written By: Kathryn Lecha
Edit Date: 2021-02-14
"""

from ...models.decision_tree import DecisionTree
from ...models.kmeans import KMeans
from ...models.knn import KNN
from ...models.lda import LDA
from ...models.random_forest_classifcation import RandomForestClassifier

from .lesson import Lesson

from ...errors import InvalidModelUse

from uuid import uuid4


MODELMAP = {
    "decision_tree": DecisionTree(),
    "kmeans": KMeans(),
    "knn": KNN(),
    "lda": LDA(),
    "random_forest_class": RandomForestClassifier()
}


class ClassificationLesson(Lesson):
    """
    Template Lesson for any classification problem
    """
    def __init__(self, uuid=str(uuid4())):
        super().__init__(uuid)
        self.lessonName = "classification"

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