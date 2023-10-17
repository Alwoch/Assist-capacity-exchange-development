from django.test import SimpleTestCase
from django.forms import Textarea
from django.utils.translation import gettext as _

from bug.forms import BugForm


class TestBugForm(SimpleTestCase):
    """
    Test suite for form in the 'bug' app.
    """

    def test_valid_form(self):
        """Tests a valid form"""
        data = {
            "description": "form does not redirect after submission",
            "bug_type": "error",
            "status": "to_do"
        }

        form = BugForm(data=data)
        self.assertTrue(form.is_valid())

    def test_required_fields(self):
        """
        Test that the form correctly handles required fields.

        Expected behavior: 
            - Submitting the form without values for required fields
        should raise validation errors
            - error messages should indicate that the fields are required
        """
        form = BugForm(data={})

        # Confirm that the form is not valid
        self.assertFalse(form.is_valid())

        # Check if the form has errors for required fields
        self.assertIn("description", form.errors)
        self.assertIn("bug_type", form.errors)
        self.assertIn("status", form.errors)

        # validating error messages for required fields
        self.assertEqual(
            form.errors["description"][0],
            "This field is required."
        )
        self.assertEqual(
            form.errors["bug_type"][0],
            "This field is required."
        )
        self.assertEqual(
            form.errors["status"][0],
            "This field is required."
        )

    def test_custom_error_messages(self):
        """
        Test that the custom error message is displayed when description is too long
        """
        data = {
            "description": "This is a very long description that should trigger the custom error message because it exceeds the maximum length allowed.",
            "bug_type": "error",
            "status": "to_do"
        }

        form = BugForm(data=data)

        # Check if the form is invalid
        self.assertFalse(form.is_valid())

        # assert that the custom error message is displayed for the "description" field
        self.assertEqual(
            form.errors["description"][0],
            _("description is too long")
        )

    def test_custom_widget_rendering(self):
        """
        Checks whether the required widgets are correctly rendered with the right columns and widths
        """
        form = BugForm()

        # Check if the "description" field uses the custom Textarea widget
        self.assertIsInstance(form.fields["description"].widget, Textarea)

        # Check if the widget's attributes are set as expected
        self.assertEqual(form.fields["description"].widget.attrs["cols"], 80)
        self.assertEqual(form.fields["description"].widget.attrs["rows"], 3)
