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
from messages.models import Message


def add(request):
    body = request.POST.get('body')
    to_user = request.POST.get('to_user')
    from_user = request.user
    if body:
        message = Message.objects.create(body=body,to_user_id=to_user,from_user=from_user)
        message.save()
        request.flash['message'] = "Message has been sent to%s"%to_user['first_name']
    return HttpResponseRedirect(reverse('message_index'))

def index(request):
    return render_to_response("messages/index.html", {}, context_instance=RequestContext(request))
