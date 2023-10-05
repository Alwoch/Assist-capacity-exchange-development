from django.contrib import admin

from .models import Bug

# registering the Bug model to the admin site
admin.site.register(Bug)
