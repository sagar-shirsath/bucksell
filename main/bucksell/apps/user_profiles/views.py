from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from datetime import date
from time import time

from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from PIL import Image
import StringIO
import os
import django
import hashlib

from django.conf import settings
from registration.backends import get_backend
from registration.forms import LoginForm
from user_profiles.forms import ProfileForm , ImageUploadForm
from user_profiles.models import Profile
from items.models import Item

def get_user_profile(id):
    user = User.objects.get(id=id)
    try:
        profile = user.auth_user.all()[0]
    except Exception:
        profile = Profile.objects.create(user_id = id)
        profile.save()
    return (user ,profile )

def home(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse("item_index"))
    items = Item.objects.filter().order_by('-publishing_date')[0:50]
    return render_to_response("user_profiles/home.html", {'items':items}, context_instance=RequestContext(request))

@login_required
def edit_profile(request):
    user , profile = get_user_profile(request.user.id)
    photo_form = ImageUploadForm()

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
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            profile = user.auth_user.all()[0]

            profile.about_me = form.cleaned_data.get('about_me')
            profile.gender = form.cleaned_data.get('gender') or 0
            profile.degree_pursuing = ""
            profile.year_of_class = form.cleaned_data.get('year_of_class') or 0
            profile.university = form.cleaned_data.get('university')
            profile.phone_number = form.cleaned_data.get('phone_number')
            profile.address = form.cleaned_data.get('address')
#            profile.paypal_url = form.cleaned_data.get('paypal_url')
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

            user.save()
            profile.save()
            if success:
                request.flash['message'] = "Profile updated successfully"

    return render_to_response("user_profiles/edit_profile.html", {'form':form ,'password_open':password_open , 'photo_form':photo_form , 'profile_photo':profile.photo}, context_instance=RequestContext(request))


def handle_uploaded_image(image,size=(100,100)):
    width , height= size
    # resize image
    imagefile  = StringIO.StringIO(image.read())
    imageImage = Image.open(imagefile)
    if imageImage.mode != "RGB":
        imageImage = imageImage.convert("RGB")
    size = imageImage.size
    if size[0] >= width or size[1] >= height :
        resizedImage = imageImage.resize((width,height),Image.ANTIALIAS)
    else:
        resizedImage = imageImage

    filename = hashlib.md5(imagefile.getvalue()).hexdigest()+'.jpg'

    # #save to disk
    imagefile = open(os.path.join('/tmp',filename), 'w')
    resizedImage.save(imagefile,'JPEG')
    imagefile = open(os.path.join('/tmp',filename), 'r')
    content = django.core.files.File(imagefile)

    return (filename, content)

def is_image(file):
    if file:
        flag = 1
        file_type = file.content_type.split('/')[0]

        if file_type in settings.IMAGE_SUPPORTED_TYPES:
            if file._size > settings.IMAGE_SUPPORTED_TYPES:
                request.flash['message'] = "Sorry Can't Upload the image , Too large size"
                flag = 0
        else:
            request.flash['message'] = "Sorry Can't Upload the image , image type is not supported"
            flag = 0
        return flag
    return 1

def upload_profile_photo(request):
    if request.method == 'POST':
        flag = 1;
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            user , profile = get_user_profile(request.user.id)
            file = form.cleaned_data.get('photo')
            if file:
                flag = is_image(file)
                if(flag):
                    if(profile.photo):
                        profile.photo.delete()
                    if(profile.thumbnail):
                        profile.thumbnail.delete()
                    user_profile_photo = handle_uploaded_image(file,settings.PROFILE_IMG_SIZE)

                    profile.photo.save("%d_%s_profile_photo.%s"%(user.id,("%s"%time())[1:6],user_profile_photo[0].split('.')[1]),user_profile_photo[1])
                    file.seek(0)
                    thumbnail = handle_uploaded_image(file,settings.PROFILE_THUMBNAILS_SIZE)
                    profile.thumbnail.save("%d_%s_profile_thumbnail.%s"%(user.id,("%s"%time())[1:6],thumbnail[0].split('.')[1]),thumbnail[1])
                    request.flash['message'] = "Photo Uploaded Successfully"
        else:
            request.flash['message'] = "Sorry Can't Upload the image"
    return HttpResponseRedirect(reverse("edit_profile"))

def login_me(request):
    if request.user.is_authenticated():
        if request.user.is_superuser:
            return HttpResponseRedirect(reverse("admin:index"))
        else:
            return HttpResponseRedirect(reverse("item_index"))
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
                        return HttpResponseRedirect(reverse("item_index"))
            request.flash['message'] = "Sorry Email and Password Does Not Match"


    return render_to_response("user_profiles/login.html" ,{'form':form} ,context_instance = RequestContext(request))
