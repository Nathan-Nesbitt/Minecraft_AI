"""
    This is a file containing all of the required errors for the Minecraft
    Education API.

    Written By: Kathryn Lecha
    Date: 2021-02-19
"""


class TypeNotFound(Exception):
    """
        Base Exception Class for all issues regarding user inputted types
        that can be handled in the game. For example if you try to create
        an event handler or "hook" for a non-existing event, for example
        "on-bounce" this can be thrown.
    """
    def __init__(self, entered_type,):
        self.message = entered_type + " is not valid Minecraft Command"
        super().__init__(self.message)

    def __str__(self):
        return f'{self.entered_type} -> {self.message}'


class ModelNotFound(TypeNotFound):
    """
        Exception which indicates that the model has not been implemented
    """
    def __init__(self, entered_type):
        self.message = entered_type + " is not an implemented model."
        super().__init__(self.message)
