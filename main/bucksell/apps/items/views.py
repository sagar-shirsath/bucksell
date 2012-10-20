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
from items.models import Item
from user_profiles.views import get_user_profile
from categories.models import Category
@login_required
def index(request):
    categories = Category.objects.all()
    return render_to_response("items/index.html", {'categories':categories}, context_instance=RequestContext(request))


def my_listing(request):
    items = Item.objects.all()
    return render_to_response("items/my_listing.html", {'items':items}, context_instance=RequestContext(request))

@login_required
def add(request):
#    user, item = get_user_profile(request.user.id)
    form = ItemForm()
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.cleaned_data['seller']= request.user
            data = form.cleaned_data
            item =  Item(
                name=data['name'],
                description =data['description'],
                condition=data['condition'],
                price=data['price'],
                longitude =data['longitude'],
                latitude=data['latitude'],
                seller =request.user,
                category =data['category']
            )
            item.save()
            return HttpResponseRedirect(reverse('my_listing'))

    return render_to_response("items/add.html", {'form': form}, context_instance=RequestContext(request))

@login_required
def edit(request):
    user, item = get_user_item(request.user.id)

    form = ItemForm(initial={
        'item_name': item.item_name,
        'price': item.price,
        'description': item.description,
        'condition': item.condition,
        'category': item.category,
        'longitude': item.longitude,
        'latitude': item.latitude
    })

    return render_to_response("items/add.html", {'form': form}, context_instance=RequestContext(request))

