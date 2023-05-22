import unittest
from event import Event

class EventTests(unittest.TestCase):
    """Subclass of TestCase for the class Event."""
    def test_init_ok(self):
        """Assert that the class properly initializes with given parameters."""
        event = Event("name", 0.99, 1)
        self.assertEqual(event.name, "name") #Should initialize all parameters properly
        self.assertEqual(event.weight, 0.99)
        self.assertEqual(event.duration, 1)

    def test_init_bad_name(self):
        """Assert that the class raises an error when given a bad name."""
        with self.assertRaises(TypeError):
            event = Event(123, 0.99, 0) #Name should be string

    def test_init_bad_weight(self):
        """Assert that the class raises an error when given a bad weight."""
        with self.assertRaises(ValueError):
            event = Event("name", -0.01, 0) #Weight should be a float, between or equal to 0 and 1.
        with self.assertRaises(ValueError):
            event = Event("name", 1.01, 0) #Weight should be a float, between or equal to 0 and 1.   
        with self.assertRaises(TypeError):
            event = Event("name", "this shouldn't work", 0) #Weight should be a float, between or equal to 0 and 1.   

    def test_init_bad_duration(self):
        """Assert that the class raises an error when given a bad duration."""
        with self.assertRaises(TypeError):
            event = Event("name", 0.99, '-0.01') #Duration should be an integer greater than or equal to 0.
        with self.assertRaises(ValueError):
            event = Event("name", 0.99, -1) #Duration should be an integer greater than or equal to 0.
