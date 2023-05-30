import datetime

class Schedule:
    """The summary line for a class docstring should fit on one line."""

    def __init__(self, name, weight, target_date):
        """Initializing the goal method.

        Args:
            name (str): Name of the goal.
            weight (:obj:`float`): Weight, or impact, of the goal.
            target_date (:obj: `datetime.datetime.date`): Target date of goal completion

        """
        self.name = name
        self.weight = weight
        self.target_date = target_date
        if not isinstance(name, str):
            raise TypeError("name should be a string")
        if not isinstance(weight, float):
            raise TypeError("weight should be a float.")
        if (weight < 0) or (weight > 1):
            raise ValueError("weight has to be between 0 and 1")
        if not isinstance(target_date, type(datetime.datetime.today().date())):
            raise TypeError("target_date has to be a date")
        if (target_date-datetime.datetime.today().date()) < datetime.timedelta(0):
            raise ValueError("target_date cannot be in the past")