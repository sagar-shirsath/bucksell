from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from datetime import date

from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from registration.backends import get_backend

from registration.forms import LoginForm


def home(request):
    return render_to_response("user_profiles/home.html", {}, context_instance=RequestContext(request))


def edit_profile(request):
    return render_to_response("user_profiles/edit_profile.html", {}, context_instance=RequestContext(request))


def edit_contacts(request):
    return render_to_response("user_profiles/edit_contacts.html", {}, context_instance=RequestContext(request))


def edit_security(request):
    return render_to_response("user_profiles/edit_security.html", {}, context_instance=RequestContext(request))


def login_me(request):
    if request.user.is_authenticated():
            if request.user.is_superuser:
                return HttpResponseRedirect(reverse("admin:index"))
            else:
                return HttpResponseRedirect(reverse("home"))
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email= form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.get(email = email)
            password_chk = user.check_password(password)
            if password_chk:
                u = authenticate( username = user.username , password = password)
                if u is not None:
                    if u.is_active:
                        login(request,u)
                        if u.is_superuser:
                            return HttpResponseRedirect(reverse("admin:index"))
                        return HttpResponseRedirect(reverse("home"))
            request.flash['message'] = "Sorry Email and Password Does Not Match"


    return render_to_response("user_profiles/login.html" ,{'form':form} ,context_instance = RequestContext(request))

