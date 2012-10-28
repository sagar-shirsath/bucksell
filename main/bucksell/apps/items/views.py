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

@login_required
def my_listing(request):
    items = Item.objects.filter(seller = request.user)
    return render_to_response("items/my_listing.html", {'items':items}, context_instance=RequestContext(request))

def upload_item_images(image1,image2,image3,item):
    thumbnail_size = (50,50)
    images_size = (192,192)
    path = settings.MEDIA_ROOT+"/images/items/"
    photo_name1 = ("%d_%s_1"%(item.id,("%s"%time())[1:6]))
    photo_name2 = ("%d_%s_2"%(item.id,("%s"%time())[1:6]))
    photo_name3 = ("%d_%s_3"%(item.id,("%s"%time())[1:6]))

    photo_thumbnail_path1 = ("%d_thumbnail_%s_1"%(item.id,("%s"%time())[1:6]))
    photo_thumbnail_path2= ("%d_thumbnail_%s_2"%(item.id,("%s"%time())[1:6]))
    photo_thumbnail_path3= ("%d_thumbnail_%s_3"%(item.id,("%s"%time())[1:6]))

    img_obj,created = ItemPhoto.objects.get_or_create(item=item)

    if image1:
        print "one"
        resized1 = handle_uploaded_image(image1,images_size)
        if(img_obj.photo1):
            img_obj.photo1.delete()
        photo1 = img_obj.photo1.save(photo_name1+resized1[0].split('.')[1],resized1[1])
        img1 = open(path+photo_name1+resized1[0].split('.')[1], 'r+')
        thumb1 = handle_uploaded_image(img1,thumbnail_size)
        if(img_obj.thumbnail1):
            img_obj.thumbnail1.delete()
        img_obj.thumbnail1.save(photo_thumbnail_path1+'.'+thumb1[0].split('.')[1],thumb1[1])

    if image2:
        print "two"
        resized2 = handle_uploaded_image(image2,images_size)
        if(img_obj.photo2):
            img_obj.photo2.delete()
        photo2 = img_obj.photo2.save(photo_name2+resized2[0].split('.')[1],resized2[1])
        img2 = open(path+photo_name2+resized2[0].split('.')[1], 'r+')
        thumb2 = handle_uploaded_image(img2,thumbnail_size)
        if(img_obj.thumbnail2):
            img_obj.thumbnail2.delete()
        img_obj.thumbnail2.save(photo_thumbnail_path2+'.'+thumb2[0].split('.')[1],thumb2[1])


    if image3:
        print "three"
        resized3 = handle_uploaded_image(image3,images_size)
        if(img_obj.photo3):
            img_obj.photo3.delete()
        photo3 = img_obj.photo3.save(photo_name3+resized3[0].split('.')[1],resized3[1])

        img3 = open(path+photo_name3+resized3[0].split('.')[1], 'r+')
        thumb3 = handle_uploaded_image(img3,thumbnail_size)
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
                category =data['category'],
                location =data['location']
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
        form = ItemForm(request.POST,request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            image1 = data['image1']
            image2 = data['image2']
            image3 = data['image3']
            if not ((is_image(image1) and is_image(image2) and is_image(image3))):
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
            request.flash['message'] = "Item saved successfully"

            return HttpResponseRedirect(reverse('my_listing'))
        else:
            request.flash['message'] = "Form data is not valid"

    return render_to_response("items/edit.html", {'form': form,'slug':slug , 'item':item}, context_instance=RequestContext(request))

@login_required
def view(request,slug=""):
    conditions = {'1': 'Mint', '2': 'Like New', '3':'Fair'}
    item = get_object_or_404(Item,slug=slug)
    return render_to_response("items/view.html", {'item':item,'conditions':conditions}, context_instance=RequestContext(request))


def search(request):
    query_string = ''
    found_entries = None
    categories = Category.objects.all()
    if ('category' in request.GET) and request.GET['category'].strip():
        found_entries = Item.objects.filter(category__icontains)
    elif ('q' in request.GET) and request.GET['q'].strip():
        item_obj = Item()
        query_string = request.GET['q']

        entry_query = item_obj.get_query(query_string, ['name', 'description','price','location'])

        found_entries = Item.objects.filter(entry_query).order_by('name')

    return render_to_response('items/index.html',
            { 'query_string': query_string,'categories':categories , 'items':found_entries},
        context_instance=RequestContext(request))
