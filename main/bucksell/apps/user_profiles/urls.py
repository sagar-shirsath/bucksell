from django.conf.urls.defaults import *

from django.contrib.auth import views as auth_views
from user_profiles import views
urlpatterns = patterns('',
    url(r'^login/$',
        views.login_me,
        name='auth_login'),
    url(r'^edit_profile/$',
        views.edit_profile,
        name='edit_profile'),

)
