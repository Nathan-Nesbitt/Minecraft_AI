"""
Predict where to mine for specific materials

Written By: Kathryn Lecha
Edit Date: 2021-02-14
"""

from .task import Task

class PredictMineTask(Task):
    """
    Class for predicting where to mine for specific materials
    """

    def __init__(self, material):
        super().__init__()
        self.material = material
    
    def read_data(self):
        """
        Read in the data
        """
        df = super().read_data("data/item_acquired.csv")

        X_columns = df.columns.drop()
        super().set_X_y()