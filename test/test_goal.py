import unittest
import datetime
from goal import Goal

class GoalTests(unittest.TestCase):
    """Subclass of TestCase for the subclass Goal of class Event."""
    def test_init_ok(self):
        """Assert that the class properly initializes with given parameters."""
        goal = Goal("name", 0.99, 1, datetime.datetime.strptime('05/25/2023','%m/%d/%Y'))
        self.assertEqual(goal.target_date, datetime.datetime.strptime('05/25/2023','%m/%d/%Y'))

    def test_init_bad_name(self):
        """Assert that the class raises an error when given a bad name."""
        with self.assertRaises(TypeError):
            goal = Goal(123, 0.99, 0, datetime.datetime.strptime('05/25/2023','%m/%d/%Y')) #Name should be string
            
    def test_init_bad_weight(self):
        """Assert that the class raises an error when given a bad weight."""
        with self.assertRaises(ValueError):
            goal = Goal("name", -0.01, 0, datetime.datetime.strptime('05/25/2023','%m/%d/%Y')) #Weight should be a float, between or equal to 0 and 1.
        with self.assertRaises(ValueError):
            goal = Goal("name", 1.01, 0, datetime.datetime.strptime('05/25/2023','%m/%d/%Y')) #Weight should be a float, between or equal to 0 and 1.   
        with self.assertRaises(TypeError):
            goal = Goal("name", "this shouldn't work", 0, datetime.datetime.strptime('05/25/2023','%m/%d/%Y')) #Weight should be a float, between or equal to 0 and 1.   

    def test_init_bad_date(self):
        """Assert that the class raises an error when given a bad date."""
        with self.assertRaises(TypeError):
            goal = Goal("name", 0.99, 0, '05/25/2023') #Date should be of datetime.datetime.date type
        with self.assertRaises(ValueError):
            goal = Goal("name", 0.99, -1, datetime.datetime.strptime('05/22/2023','%m/%d/%Y')) #Date should not be in the past.