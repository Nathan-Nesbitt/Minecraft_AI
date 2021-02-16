"""
Predict best animals to farm based on types (XP, Food, ect)

Written By: Kathryn Lecha
Edit Date: 2021-02-08
"""

from task import Task

class PredictFarm(Task):
    """
    Predict what the best animal to farm is for a given type
    """
    def __init__(self, resource):
        self.resource = resource
        self.model=None
    
    def set_model(self, model):
        """
        set the model the player will use
        """
        
