import unittest
from exam_info import exam_info
import datetime
exam_info=exam_info()
class TestExamInfo(unittest.TestCase):
    """Testing the exam_info() function."""
    def test_subject_getter_assert_list(self):
        """Tests if the exam_info class's subject_getter() function returns a list.

        Returns:
            True if successful, False otherwise.
        """
        subjects=exam_info.subject_getter()
        self.assertIsInstance(subjects,list, f"Test subjects should be of type 'list', but actually are {type(subjects)}")
        for i, element in enumerate(subjects):
            self.assertIsInstance(element,str, f"Test subjects {i} should be of type 'str', but actually are {type(element)}")
    def test_date_getter_assert_list(self):
        """Tests if the exam_info class's date_getter() function returns a list.

        Returns:
            True if successful, False otherwise.
        """
        self.assertIsInstance(exam_info.date_getter(), list, f"Test date array should be of type 'list', but actually are {type(exam_info.date_getter())}")
        for i, element in enumerate(exam_info.date_getter()):
            self.assertIsInstance(element, datetime.date, f"Test date {i+1} should be of type 'datetime.date', but actually are {type(element)}")
    def test_days_remaining_getter_assert_int(self):
        """Tests the integrity of the exam_info class's days_remaining() function.

        Returns:
            True if successful, False otherwise.
        """
        dates=exam_info.days_remaining_getter()
        self.assertIsInstance(dates, list, f"The array containing number of days remaining until exams should be of type 'list', but actually are {type(dates)}")
        for i, element in dates:
            calculated_exam_date=datetime.datetime.today().date+datetime.timedelta(days=element)
            self.assertIsInstance(element, int, f"The number of days remaining for subject {i+1} should be of type 'datetime.date', but actually are {type(element)}")
            self.assertEquals(calculated_exam_date, dates[i], f"The number of days remaining, when added to the current date today, should equal {dates[i]}, but actually equals {calculated_exam_date}")
if __name__ == '__main__':
    unittest.main()