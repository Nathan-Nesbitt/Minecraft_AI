"""
    This is a file containing all of the required errors for the Minecraft
    Education API.

    Written By: Kathryn Lecha
    Date: 2021-02-12
"""


class TypeNotFound(Exception):
    """
        Base Exception Class for all issues regarding user inputted types
        that can be handled in minecraft_learns. For example if you try to
        a model that does not exist, for example "qda" this can be thrown.
    """
    def __init__(
        self, entered_type,
        message="The type of Model or Lesson was not Found"
    ):
        self.entered_type = entered_type
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.entered_type} -> {self.message}'


class TaskNotFound(TypeNotFound):
    """
        Exception which indicates that the task has not been implemented
    """
    def __init__(self, entered_type):
        super().__init__(
            entered_type,
            "The Entered Task does not exist"
        )


class ModelNotFound(TypeNotFound):
    """
        Exception which indicates that the model has not been implemented
    """
    def __init__(self, entered_type):
        super().__init__(
            entered_type,
            "The entered Model was not found"
        )


class InvalidInputUse(ValueError):
    """
        Error class that defines all invalid inputs from the user
        For example if you try to use a classification model for a regression
        problem, this can be thrown.
    """
    def __init__(
        self, entered_type,
        message="The input cannot be used here"
    ):
        self.entered_type = entered_type
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.entered_type} -> {self.message}'
    

class InvalidModelUse(InvalidInputUse):
    """
        Exception which indicates that the model cannot be used there
    """
    def __init__(self, entered_type):
        super().__init__(
            entered_type,
            "The entered Model cannot be used here"
        )


class InvalidDataUse(InvalidInputUse):
    """
        Exception which indicates that the data cannot be used there
    """
    def __init__(self, entered_type):
        super().__init__(
            entered_type,
            "The entered data cannot be used here"
        )


class IncorrectFlow(Exception):
    """
        Error class that defines all flow errors during user tasks
        For example if the user tries to predict without fitting, this error
        can be thrown
    """
    def __init__(
        self, entered_type,
        message="The method cannot be executed yet"
    ):
        self.entered_type = entered_type
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.entered_type} -> {self.message}'


class UnProcessedData(IncorrectFlow):
    """
        Exception which indicates that the data has not been processed
    """
    def __init__(self, entered_type):
        super().__init__(
            entered_type,
            "The data has not been processed yet"
        )


class ModelNotFit(IncorrectFlow):
    """
        Exception which indicates that the model has not been fit yet
    """
    def __init__(self, entered_type):
        super().__init__(
            entered_type,
            "The model has not been fit yet"
        )


class NoPrediction(IncorrectFlow):
    """
        Exception which indicates that there is no prediction to execute
    """
    def __init__(self, entered_type):
        super().__init__(
            entered_type,
            "There is no prediction to execute"
        )
