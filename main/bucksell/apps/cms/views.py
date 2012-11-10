from django.shortcuts import render_to_response
from django.template import RequestContext

def about(request):
    return render_to_response("cms/about.html", context_instance=RequestContext(request))

def pricing(request):
    return render_to_response("cms/pricing.html", context_instance=RequestContext(request))

def help(request):
    return render_to_response("cms/help.html", context_instance=RequestContext(request))

def terms(request):
    return render_to_response("cms/terms.html", context_instance=RequestContext(request))

def privacy(request):
    return render_to_response("cms/privacy.html", context_instance=RequestContext(request))

def jobs(request):
    return render_to_response("cms/jobs.html", context_instance=RequestContext(request))

def blogs(request):
    return render_to_response("cms/blogs.html", context_instance=RequestContext(request))

def timeline(request):
    return render_to_response("cms/timeline.html", context_instance=RequestContext(request))