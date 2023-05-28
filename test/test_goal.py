import unittest
import datetime
from goal import Goal

class GoalTests(unittest.TestCase):
    """Subclass of TestCase for the subclass Goal of class Event."""
    def test_init_ok(self):
        """Assert that the class properly initializes with given parameters."""
        goal = Goal("name", 0.99, datetime.datetime.today.date()+datetime.timedelta(days=3))
        self.assertEqual(goal.name, "name") #Should initialize all parameters properly
        self.assertEqual(goal.weight, 0.99)
        self.assertEqual(goal.target_date, datetime.datetime.today.date()+datetime.timedelta(days=3))

    def test_init_bad_name(self):
        """Assert that the class raises an error when given a bad name."""
        with self.assertRaises(TypeError):
            goal = Goal(123, 0.99, datetime.datetime.today.date()+datetime.timedelta(days=3)) #Name should be string
            
    def test_init_bad_weight(self):
        """Assert that the class raises an error when given a bad weight."""
        with self.assertRaises(ValueError):
            goal = Goal("name", -0.01, datetime.datetime.today.date()+datetime.timedelta(days=3)) #Weight should be a float, between or equal to 0 and 1.
        with self.assertRaises(ValueError):
            goal = Goal("name", 1.01, datetime.datetime.today.date()+datetime.timedelta(days=3)) #Weight should be a float, between or equal to 0 and 1.   
        with self.assertRaises(TypeError):
            goal = Goal("name", "this shouldn't work", datetime.datetime.today.date()+datetime.timedelta(days=3)) #Weight should be a float, between or equal to 0 and 1.   

    def test_init_bad_date(self):
        """Assert that the class raises an error when given a bad date."""
        with self.assertRaises(TypeError):
            goal = Goal("name", 0.99, '05/25/2023') #target_date should be of datetime.datetime.date type
        with self.assertRaises(ValueError):
            goal = Goal("name", 0.99, datetime.datetime.today.date()+datetime.timedelta(days=-1)) #Date should not be in the past.