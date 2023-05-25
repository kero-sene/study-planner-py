import datetime

class Goal:
    """The summary line for a class docstring should fit on one line."""

    def __init__(self, name, weight, duration, date):
        """Initializing the goal method.

        Args:
            name (str): Name of the goal.
            weight (:obj:`float`): Weight, or impact, of the goal.
            duration (:obj:`int`): Duration of the goal.
            date (:obj: `datetime.datetime.date`): Target date of goal completion

        """
        self.name = name
        self.weight = weight
        self.duration = duration
        self.date = date
        if not isinstance(name, str):
            raise TypeError("name should be a string")
        if not isinstance(weight, float):
            raise TypeError("weight should be a float.")
        if (weight < 0) or (weight > 1):
            raise ValueError("weight has to be between 0 and 1")
        if not isinstance(date, datetime.datetime.date):
            raise TypeError("duration has to be an integer")
        if date <= 0:
            raise ValueError("duration has to be more than 0")
    def example_method(self, name, param2):
        """Class methods are similar to regular functions.

        Note:
            Do not include the `self` parameter in the ``Args`` section.

        Args:
            param1: The first parameter.
            param2: The second parameter.

        Returns:
            True if successful, False otherwise.

        """
        return True