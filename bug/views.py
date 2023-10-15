from django.shortcuts import render, get_object_or_404,redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import DetailView

# import the model
from .models import Bug

from .forms import BugForm


def register_bug(request):
    """
    Renders the bug registration page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponseRedirect: List of all the bugs including the one added
    """
    if request.method == 'POST':
        form = BugForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('bug:get_all_bugs'))
    else:
        form = BugForm()

    return render(request, 'bug/register.html', {'form': form})


def bug_detail(request, bug_id):
    """
    Renders the bug detail page for a specific bug.

    Args:
        request (HttpRequest): The HTTP request object.
        bug_id (int): The ID of the bug to display details for.

    Returns:
        HttpResponse: The rendered bug detail page.

    Raises:
        Http404: If the specified bug_id does not exist in the database.
    """
    bug = get_object_or_404(Bug, pk=bug_id)

    return render(request, "bug/detail.html", {"bug": bug})


def get_all_bugs(request):
    """
    Displays a list of all bugs with the most recent bug appearing at the top.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered page with a list of bugs.
    """
    bugs_list = Bug.objects.all().order_by("-report_date")
    context = {"bugs_list": bugs_list}

    return render(request, "bug/index.html", context)
