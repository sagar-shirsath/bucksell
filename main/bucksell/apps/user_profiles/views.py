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

from user_profiles.forms import ProfileForm

from user_profiles.models import Profile


def home(request):
    return render_to_response("user_profiles/home.html", {}, context_instance=RequestContext(request))

@login_required
def edit_profile(request):
    user = User.objects.get(id=request.user.id)
    profile = user.auth_user.all()[0]

    form = ProfileForm(initial={
        'first_name':user.first_name,
        'last_name':user.last_name,
        'about_me':profile.about_me,
         'gender':profile.gender,
        'degree_pursuing':profile.degree_pursuing,
        'year_of_class':profile.year_of_class,
        'phone_number':profile.phone_number,
        'address':profile.address,
        'university':profile.university,
        'paypal_url':profile.paypal_url,
        'zip_code':profile.zip_code,
        'visibility':profile.visibility,

    })

    password_open = 0
    success = 1
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            print form.cleaned_data

            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            profile = user.auth_user.all()[0]

            profile.about_me = form.cleaned_data.get('about_me')
            profile.gender = form.cleaned_data.get('gender') or 0
            profile.degree_pursuing = form.cleaned_data.get('degree_pursuing')
            profile.year_of_class = form.cleaned_data.get('year_of_class') or 0
            ##            profile.university = form.cleaned_data.get('university')
            profile.phone_number = form.cleaned_data.get('phone_number')
            profile.address = form.cleaned_data.get('address')
            profile.paypal_url = form.cleaned_data.get('paypal_url')
            profile.zip_code = form.cleaned_data.get('zip_code')

            profile.visibility = int(form.cleaned_data.get('visibility') or 0)

            if form.cleaned_data.get('current_password'):
                password_check = user.check_password(form.cleaned_data.get('current_password'))
                if (password_check) and (form.cleaned_data.get('new_password')==form.cleaned_data.get('confirm_password')):
                    user.set_password(form.cleaned_data.get('new_password'))
                else:
                    password_open = 1
                    success = 0
                    request.flash['message'] = "Password does not match , Pleas try again"

            print profile
            user.save()
            profile.save()
            if success:
                request.flash['message'] = "Profile updated successfully"

    return render_to_response("user_profiles/edit_profile.html", {'form':form ,'password_open':password_open}, context_instance=RequestContext(request))


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
            try:
                user = User.objects.get(email = email)
            except:
                user = None

            if user and user.check_password(password):
                u = authenticate( username = user.username , password = password)
                if u is not None:
                    if u.is_active:
                        login(request,u)
                        if u.is_superuser:
                            return HttpResponseRedirect(reverse("admin:index"))
                        return HttpResponseRedirect(reverse("home"))
            request.flash['message'] = "Sorry Email and Password Does Not Match"


    return render_to_response("user_profiles/login.html" ,{'form':form} ,context_instance = RequestContext(request))

