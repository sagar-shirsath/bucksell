from django.contrib import admin
from django.contrib.auth.models import Group
from registration.models import RegistrationProfile
admin.site.unregister(Group)
admin.site.unregister(RegistrationProfile)