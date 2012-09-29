from django.conf.urls.defaults import *

from django.contrib.auth import views as auth_views
from user_profiles import views
urlpatterns = patterns('',
    url(r'^edit_profile/$',
        views.edit_profile,
        name='edit_profile'),
    url(r'^edit_contacts/$',
        views.edit_contacts,
        name='edit_contacts'),
    url(r'^edit_security/$',
        views.edit_security,
        name='edit_security'),

)
