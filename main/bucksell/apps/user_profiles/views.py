from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login , authenticate, logout
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from datetime import date

from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from registration.backends import get_backend



def home(request):
    return render_to_response("user_profiles/home.html" ,{} ,context_instance = RequestContext(request))
def edit_profile(request):
    return render_to_response("user_profiles/edit_profile.html" ,{} ,context_instance = RequestContext(request))
def edit_contacts(request):
    return render_to_response("user_profiles/edit_contacts.html" ,{} ,context_instance = RequestContext(request))
def edit_security(request):
    return render_to_response("user_profiles/edit_security.html" ,{} ,context_instance = RequestContext(request))


