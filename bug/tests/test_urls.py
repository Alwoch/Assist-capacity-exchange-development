from django.test import SimpleTestCase
from django.urls import reverse, resolve
from bug.views import register_bug, bug_detail, get_all_bugs


class TestBugUrls(SimpleTestCase):
    """
    Test suite for url routing in the 'bug' app.
    """

    def test_get_all_bugs_url_resolves(self):
        """
        Test whether the 'get_all_bugs' url correctly resolves to the get_all_bugs function.
        """
        url = reverse("bug:get_all_bugs")
        self.assertEqual(resolve(url).func, get_all_bugs)

    def test_bug_detail_url_resolves(self):
        """
        Test whether the 'bug_detail' url correctly resolves to the bug_detail function.
        """
        url = reverse("bug:bug_detail", args=[1])
        self.assertEqual(resolve(url).func, bug_detail)

    def test_register_bug_url_resolves(self):
        """
        Test whether the 'register_bug' url correctly resolves to the register_bug function.
        """
        url = reverse("bug:register_bug")
        self.assertEqual(resolve(url).func, register_bug)
