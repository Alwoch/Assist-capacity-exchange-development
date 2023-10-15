from django.forms import ModelForm, Textarea
from django.utils.translation import gettext_lazy as _

from .models import Bug


class BugForm(ModelForm):
    """
    Form class for creating and validating a Bug.
    """

    class Meta:
        """
        Metadata options for the BugForm class.

        Attributes:
            model (Bug): The model associated with this form.
            fields (list): The fields from the model to include in the form.
            widgets (dict): Custom widgets for form fields.
            error_messages (dict): Custom error messages for form fields.
        """
        model = Bug
        fields = ['description', 'bug_type', 'status']
        widgets = {
            "description": Textarea(attrs={"cols": 80, "rows": 3}),
        }
        error_messages = {
            "description": {
                "max_length": _("description is too long"),
            },
        }
