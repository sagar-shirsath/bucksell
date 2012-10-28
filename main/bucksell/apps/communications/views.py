# Create your views here.
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from datetime import date
from django.conf import settings
import os
from time import time
from communications.models import Message


def add(request):
    body = request.POST.get('body')
    to_user = request.POST.get('to_user')
    item_slug = request.POST.get('item_slug')
    from_user = request.user
    if body and (from_user!=to_user):
        message = Message.objects.create(body=body,to_user_id=to_user,from_user=from_user)
        message.save()
        request.flash['message'] = "Message has been sent"
    request.flash['message'] = "Its your item!!!"
    return HttpResponseRedirect(reverse('item_view',args=(item_slug,)))

def index(request):
    messages = Message.objects.all()
    return render_to_response("messages/index.html", {'messages':messages}, context_instance=RequestContext(request))
