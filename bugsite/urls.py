from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("bug/", include("bug.urls")),
    path('admin/', admin.site.urls),
]
