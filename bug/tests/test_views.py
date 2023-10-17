import os
import json

from django.test import TestCase, Client
from django.urls import reverse

from bug.models import Bug


class TestBugViews(TestCase):
    """
    Test suite for views in the 'bug' app.
    """

    def setUp(self):
        """
        - Common resources and urls for testing views in the 'bug' app.

        Attributes:
            client (Client): The Django test client for making HTTP requests.
            bugs_list_url (str): url for listing all bugs.
            bug_detail_url (str): url for viewing a bug detail (assumes bug with ID 1).
            create_bug_url (str): url for creating a new bug.
            fixture_data: sample bugs for the test database
        """
        self.client = Client()
        self.bugs_list_url = reverse("bug:get_all_bugs")
        self.bug_detail_url = reverse("bug:bug_detail", args=[1])
        self.create_bug_url = reverse("bug:register_bug")

        # loading the fixture data
        fixture_path = os.path.join(
            os.path.dirname(__file__), "bug_fixture.json")

        with open(fixture_path, 'r') as fixture_file:
            fixture_data = json.load(fixture_file)
            self.fixture_data = fixture_data

        # adding the fixture_data to the test database
        for record in self.fixture_data:
            Bug.objects.create(**record)

    def test_get_all_bugs_view(self):
        """
        Tests the 'get_all_bugs' view to ensure it returns the expected response.

        Expected Behavior:
            - The response status code should be 200.
            - The 'bug/index.html' template should be rendered.
        """
        response = self.client.get(self.bugs_list_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "bug/index.html")

    def test_bug_detail_view(self):
        """
        Tests the 'bug_detail' view to ensure it returns the expected response.

        Expected Behavior:
            - The response status code should be 200.
            - The 'bug/detail.html' template should be rendered
            - The response status code should be 404 when the bug does not exist.
        """
        response = self.client.get(self.bug_detail_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "bug/detail.html")

    def test_register_bug_view(self):
        """
        Tests the register_bug view for valid bug registration

        Expected Behaviour:
            - created bug must be present in the database
            - must redirect to the get_all_bugs view after successfully posting data
        """
        post_data = {
            "description": "Test Bug",
            "bug_type": "error",
            "status": "to_do"
        }

        response = self.client.post(self.create_bug_url, post_data)

        self.assertTrue(Bug.objects.filter(description="Test Bug").exists())
        self.assertRedirects(response, reverse("bug:get_all_bugs"))


    def test_register_bug_view_invalid_data(self):
        """
        Tests the register_bug view for invalid bug registration

        Expected Behaviour:
            - created bug must not be created in the database
            - 'bug/register.html' template must be used
            - The form in the response context should be invalid
            - The response fails with a status code of 200
        """
        # Invalid post data with missing fields
        post_data = {
            "bug_type": "error"
        }

        response = self.client.post(reverse("bug:register_bug"), post_data)

        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context["form"].is_valid())
        self.assertTemplateUsed(response, "bug/register.html")
        self.assertFalse(Bug.objects.filter(description="Test Bug").exists())
