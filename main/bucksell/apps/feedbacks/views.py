
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from datetime import date
from time import time
from feedbacks.forms import FeedbckForm
from feedbacks.models import Feedback

@login_required()
def add(request):
    user = request.user.id
    form = FeedbckForm()
    if request.method == 'POST':
        form = FeedbckForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data.get('message')
            subject = form.cleaned_data.get('subject')
            print request.user
            from_user = request.user
            to_user = 2
            item = 1
            if message:
                feedback = Feedback(body = message , subject = subject , from_user=from_user , to_user_id=to_user , item_id = item)
                feedback.save()

    return render_to_response("items/add_feedback.html", {'form':form}, context_instance=RequestContext(request))
@login_required()
def feedbacks(request):
    user = request.user.id
    form = FeedbckForm()
    return render_to_response("items/feedbacks.html", {'form':form}, context_instance=RequestContext(request))

