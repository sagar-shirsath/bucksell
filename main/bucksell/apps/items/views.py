from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from datetime import date
from items.forms import ItemForm
from items.models import Item, ItemPhoto
from user_profiles.views import get_user_profile,is_image ,handle_uploaded_image
from categories.models import Category
from django.conf import settings
import os
from time import time

@login_required
def index(request):
    categories = Category.objects.all()
    items = Item.objects.all()
    return render_to_response("items/index.html", {'categories':categories , 'items':items}, context_instance=RequestContext(request))


def my_listing(request):
    items = Item.objects.filter(seller = request.user)
    return render_to_response("items/my_listing.html", {'items':items}, context_instance=RequestContext(request))

def upload_item_images(image1,image2,image3,item):
    size = (50,50)
    path = settings.MEDIA_ROOT+"/images/items/"
    photo_name1 = ("%d_%s_1.%s"%(item.id,("%s"%time())[1:6],"jpg"))
    photo_name2 = ("%d_%s_2.%s"%(item.id,("%s"%time())[1:6],"jpg"))
    photo_name3 = ("%d_%s_3.%s"%(item.id,("%s"%time())[1:6],"jpg"))

    photo_thumbnail_path1 = ("%d_thumbnail_%s_1.%s"%(item.id,("%s"%time())[1:6],"jpg"))
    photo_thumbnail_path2= ("%d_%s_2%s"%(item.id,("%s"%time())[1:6],item.slug))
    photo_thumbnail_path3= ("%d_%s_3%s"%(item.id,("%s"%time())[1:6],item.slug))

    img_obj,created = ItemPhoto.objects.get_or_create(item=item)


    if(img_obj.photo1):
        img_obj.photo1.delete()
    photo1 = img_obj.photo1.save(photo_name1,image1)
    img1 = open(path+photo_name1, 'r+')
    thumb1 = handle_uploaded_image(img1,size)
    if(img_obj.thumbnail1):
        img_obj.thumbnail1.delete()
    img_obj.thumbnail1.save(photo_thumbnail_path1+'.'+thumb1[0].split('.')[1],thumb1[1])


    if(img_obj.photo2):
        img_obj.photo2.delete()
    photo2 = img_obj.photo2.save(photo_name2,image2)
    img2 = open(path+photo_name2, 'r+')
    thumb2 = handle_uploaded_image(img2,size)
    if(img_obj.thumbnail2):
        img_obj.thumbnail2.delete()
    img_obj.thumbnail2.save(photo_thumbnail_path2+'.'+thumb2[0].split('.')[1],thumb2[1])


    if(img_obj.photo3):
        img_obj.photo3.delete()
    photo3 = img_obj.photo3.save(photo_name3,image3)

    img3 = open(path+photo_name3, 'r+')
    thumb3 = handle_uploaded_image(img3,size)
    if(img_obj.thumbnail3):
        img_obj.thumbnail3.delete()
    img_obj.thumbnail3.save(photo_thumbnail_path3+'.'+thumb3[0].split('.')[1],thumb3[1])

    img_obj.save()
    return img_obj
@login_required
def add(request):
#    user, item = get_user_profile(request.user.id)
    form = ItemForm()
    if request.method == "POST":
        form = ItemForm(request.POST,request.FILES)
        if form.is_valid():
            form.cleaned_data['seller']= request.user
            data = form.cleaned_data
            image1 = data['image1']
            image2 = data['image2']
            image3 = data['image3']
            if not (is_image(image1) and is_image(image2) and is_image(image3)):
                request.flash['message'] = "Sorry can't Upload the Images"
                return HttpResponseRedirect(reverse('add_item'))
            item =  Item(
                name=data['name'],
                description =data['description'],
                condition=data['condition'],
                price=data['price'],
                longitude =data['longitude'] or 0,
                latitude=data['latitude'] or 0,
                seller =request.user,
                category =data['category']
            )

            item_obj = item.save()
            upload_item_images(image1,image2,image3,item)
            request.flash['message'] = "Item saved successfully"

        #            else:
        #                request.flash['message'] = "Sorry can't save item"
            return HttpResponseRedirect(reverse('my_listing'))
        else:
            request.flash['message'] = "Invalid data"


    return render_to_response("items/add.html", {'form': form}, context_instance=RequestContext(request))

@login_required
def edit(request,slug=""):
    item = get_object_or_404(Item,slug=slug)
    if(item.seller != request.user):
        request.flash['message'] = "Sorry you are not authorised to edit this item"
        return HttpResponseRedirect(reverse('my_listing'))

    form = ItemForm(initial={
        'name': item.name,
        'price': item.price,
        'description': item.description,
        'condition': item.condition,
        'price': item.price,
        'longitude': item.longitude,
        'latitude': item.latitude,
        'category': item.category
    })

    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            image1 = data['image1']
            image2 = data['image2']
            image3 = data['image3']
            if not (is_image(image1) and is_image(image2) and is_image(image3)):
                request.flash['message'] = "Sorry can't Upload the Images"
                return HttpResponseRedirect(reverse('add_item'))
            item.name =data['name']
            item.description =data['description']
            item.condition=data['condition']
            item.price=data['price']
            item.longitude =data['longitude'] or 0
            item.latitude=data['latitude'] or 0
            item.seller =request.user
            item.category =data['category']
            item.save()
            upload_item_images(image1,image2,image3,item)
            if(item.save()):
                request.flash['message'] = "Item saved successfully"
            else:
                request.flash['message'] = "Sorry can't save item"

            return HttpResponseRedirect(reverse('my_listing'))
        else:
            request.flash['message'] = "Form data is not valid"

    return render_to_response("items/edit.html", {'form': form,'slug':slug , 'item':item}, context_instance=RequestContext(request))

def view(request,slug=""):

    return render_to_response("items/views.html", {}, context_instance=RequestContext(request))
