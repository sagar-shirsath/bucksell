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
    if request.method == "POST":
        body = request.POST.get('body')
        to_user = request.POST.get('to_user')
        item_slug = request.POST.get('item_slug')
        from_user = request.user
        message = Message.objects.create(body=body,to_user_id=to_user,from_user=from_user)
        message.save()
        request.flash['message'] = "Message has been sent"
        request.flash['message'] = "Its your item!!!"
    return HttpResponseRedirect(reverse('item_view',args=(item_slug,)))

def index(request):
    messages = Message.objects.filter(to_user=request.user  )
    return render_to_response("messages/index.html", {'messages':messages}, context_instance=RequestContext(request))

def delete(request,id):
    messages = get_object_or_404(Message , id=id)
    messages.delete()
    request.flash['message'] = "Message has been deleted"
    return HttpResponseRedirect(reverse('message_index'))

def reply(request):
    print "Hiiii"
    if request.method == "POST":
        body = request.POST.get('body')
        to_user = request.POST.get('from_user')
        from_user = request.user
        message = Message.objects.create(body=body,to_user_id=to_user,from_user=from_user)
        message.save()
        request.flash['message'] = "Message has been sent"

    return HttpResponseRedirect(reverse('message_index'))


