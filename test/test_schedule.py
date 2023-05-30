import unittest
from scheduler import Schedule
import pandas as pd
import datetime
'''The point of the schedule is to create potential "solution" schedules
in the form of a dictionary.
These may or may not be optimal, but the optimizer will come later.'''

class ScheduleTests(unittest.TestCase):
    """Subclass of TestCase for the Schedule class."""
    def test_init_ok(self):
        """Assert that the class properly initializes with given parameters."""
        schedule = Schedule(int('05134'), datetime.datetime.today().date()+datetime.timedelta(days=3))
        self.assertEqual(schedule.id, int('05134')) #Should initialize all parameters properly
        self.assertEqual(schedule.end_date, datetime.datetime.today().date()+datetime.timedelta(days=3))

    def test_init_bad_id(self):
        """Assert that the class raises an error when given a bad id."""
        with self.assertRaises(TypeError):
            schedule = Schedule('123', datetime.datetime.today().date()+datetime.timedelta(days=3)) #Name should be string
    def test_init_bad_date(self):
        """Assert that the class raises an error when given a bad date."""
        with self.assertRaises(TypeError):
            schedule = Schedule(int(431058), '05/28/2023') #Date should be datetime.datetime.date
        with self.assertRaises(ValueError):
            schedule = Schedule(int(431058), datetime.datetime.today().date()+datetime.timedelta(days=-1)) #Date cannot be in the past
