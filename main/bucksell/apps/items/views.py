from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login , authenticate, logout
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from datetime import date


def index(request):
    return render_to_response("items/index.html" ,{} ,context_instance = RequestContext(request))

def add(request):
    return render_to_response("items/add.html" ,{} ,context_instance = RequestContext(request))

