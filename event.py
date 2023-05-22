class Event():
    """Defines the abstract 'Event', which all subclasses of the program will fall under."""
    
    def __init__(self, name, weight, duration):
        """Initializes an event.

        Args:
            name (str): Name of the event.
            duration (:obj:`int`): Duration of the event in minutes.
            weight (:obj:`float` of :obj:`str`): Description of `param3`.

        """
        self.name = name  #: Sets "name" attribute to the "name" parameter
        self.weight = weight  #: Sets "weight" attribute to the "weight" parameter
        self.duration = duration  #: Sets "duration" attribute to the "duration" parameter
        if not isinstance(name, str):
           raise TypeError("name should be a string")
        if not isinstance(weight, float):
            raise TypeError("weight should be a float.")
        if (weight < 0) or (weight > 1):
            raise ValueError("weight has to be between 0 and 1")
        if not isinstance(duration, int):
            raise TypeError("duration has to be an integer")
        if duration <= 0:
            raise ValueError("duration has to be more than 0")