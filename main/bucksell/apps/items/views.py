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

def get_user_item(id):
	user = User.objects.get(id=id)
	try:
		item = user.auth_user.all()[0]
	except Exception:
		item = Item.objects.create(seller_id=id)
		item.save()
	return (user, item)


@login_required
def index(request):
	return render_to_response("items/index.html", {}, context_instance=RequestContext(request))


@login_required
def add(request):
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

	return render_to_response("items/add.html", {'form':form}, context_instance=RequestContext(request))

