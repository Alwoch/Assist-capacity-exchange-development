from django.db import models
from django.utils.translation import gettext_lazy as _

# bug model
class Bug(models.Model):
    """
    A model to represent a bug report in the bug tracking system.

    Attributes:
        description (str): A textual description of the bug.
        bug_type (str): The type of the bug (e.g., 'error', 'feature', 'other').
        report_datetime (datetime): The date and time when the bug is registered.
        status (str): The status of the bug resolution (e.g., 'to_do', 'in_progress', 'done').
    """
    # allowed descriptions of bug types
    BUG_TYPES = (
        ('error', _('Error')),
        ('feature', _('New Feature')),
        ('other', _('Other')),
    )

    # allowed bug status choices
    STATUS_CHOICES = (
        ('to_do', _('To Do')),
        ('in_progress', _('In Progress')),
        ('done', _('Done')),
    )

    description = models.CharField(max_length=120)
    bug_type = models.CharField(
        max_length=70, choices=BUG_TYPES, default='error')
    report_date = models.DateField(auto_now_add=True)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='to_do')

    def __str__(self):
        """
        Creates a human-readable representation of the bug.

        Returns:
            str: The bug's description.
        """
        return self.description

