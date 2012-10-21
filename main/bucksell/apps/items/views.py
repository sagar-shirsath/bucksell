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
from user_profiles.views import get_user_profile,is_image
from categories.models import Category



@login_required
def index(request):
    categories = Category.objects.all()
    return render_to_response("items/index.html", {'categories':categories}, context_instance=RequestContext(request))


def my_listing(request):
    items = Item.objects.all()
    return render_to_response("items/my_listing.html", {'items':items}, context_instance=RequestContext(request))

def upload_item_images(image1,image2,image3,item_id):
    img_obj = ItemPhoto(item=item_id)
    img_obj.photo = image1
    img_obj.save()
    return True
@login_required
def add(request):
#    user, item = get_user_profile(request.user.id)
    form = ItemForm()
    if request.method == "POST":
        form = ItemForm(request.POST,request.FILES)
        print(request.POST);
        if form.is_valid():
            form.cleaned_data['seller']= request.user
            data = form.cleaned_data
            image1 = form.cleaned_data['image1']
            image2 = form.cleaned_data['image2']
            image3 = form.cleaned_data['image3']
            if is_image(image1) and is_image(image2) and is_image(image3):
                request.flash['message'] = "Sorry can't Upload the Images"
                return HttpResponseRedirect(reverse('add'))
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
            if(item_obj):
                request.flash['message'] = "Item saved successfully"
            else:
                request.flash['message'] = "Sorry can't save item"
            return HttpResponseRedirect(reverse('add'))
        else:
            request.flash['message'] = "Invalid data"
            image_id = upload_item_images(image1,image2,image3,item.id)

    return render_to_response("items/add.html", {'form': form}, context_instance=RequestContext(request))

@login_required
def edit(request,slug=""):
    print  slug
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
        print(request.POST);
        if form.is_valid():
            data = form.cleaned_data
            item.name =data['name']
            item.description =data['description']
            item.condition=data['condition']
            item.price=data['price']
            item.longitude =data['longitude'] or 0
            item.latitude=data['latitude'] or 0
            item.seller =request.user
            item.category =data['category']
            item.save()
            if(item.save()):
                request.flash['message'] = "Item saved successfully"
            else:
                request.flash['message'] = "Sorry can't save item"

            return HttpResponseRedirect(reverse('my_listing'))
        else:
            request.flash['message'] = "Form data is not valid"

    return render_to_response("items/edit.html", {'form': form,'slug':slug}, context_instance=RequestContext(request))

def view(request):

	return render_to_response("items/views.html", {}, context_instance=RequestContext(request))
