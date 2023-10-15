from django.urls import path

from . import views

app_name = "bug"
urlpatterns = [
    path("", views.get_all_bugs, name="get_all_bugs"),
    path("<int:bug_id>/", views.bug_detail, name="bug_detail"),
    path("register-bug", views.register_bug, name="register_bug")
]