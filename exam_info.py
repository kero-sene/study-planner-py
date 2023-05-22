class exam_info():
    """The exam info class is meant to contain methods for gathering user input regarding exams."""

    def __init__(self):
        """Initializing the exam_info class object."""
    def subject_getter(self):
        """Prompts user input for upcoming exam subjects.

        Returns:
            List of exam subjects.
        """
        subjects=[]
        user_input_subjects = input("What exams would you like to generate a schedule for? Please separate each with a comma.\n").split(',')
        for subject in user_input_subjects:
            subjects.append(subject.strip())
        return subjects
    def date_getter(self):
        """Class methods are similar to regular functions.

        Note:
            Do not include the `self` parameter in the ``Args`` section.

        Args:
            param1: The first parameter.
            param2: The second parameter.

        Returns:
            True if successful, False otherwise.

        """
        return [0,0]
    def days_remaining_getter(self):
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

if __name__ == '__main__':
    exam_info=exam_info()