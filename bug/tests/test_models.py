from django.test import TestCase

from bug.models import Bug


class TestBugModel(TestCase):
    """
    Test suite for models in the 'bug' app.
    """

    def setUp(self):
        """create a bug to be run with the tests"""

        self.bug = Bug.objects.create(
            description="form does not redirect after submission",
            bug_type="error",
            status="to-do"
        )

    def test_new_bug_creation(self):
        """
        - Tests whether the created bug in set up is an instance of the bug model
        - Tests whether the bug exists in the database
        """
        self.assertTrue(isinstance(self.bug, Bug))
        self.assertTrue(Bug.objects.filter(
            description="form does not redirect after submission"
            ).exists())
        

    def test_str_returns_description(self):
        """
        Tests whether the model's __str__() function correctly returns the description
        """
        self.assertEquals(self.bug.__str__(), self.bug.description)


    def test_report_date_field(self):
        """
        Confirms that the report_date is set on save
        """
        self.assertIsNotNone(self.bug.report_date)


    def test_bug_type_field_valid_choices(self):
        """
        Test that the bug_type field is one of the valid choices
        """
        valid_bug_types = [choice[0] for choice in Bug.BUG_TYPES]
        self.assertIn(self.bug.bug_type, valid_bug_types)


