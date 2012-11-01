# Create your views here.


def cancelled(request):
    return render_to_response("payments/cancelled.html", {}, context_instance=RequestContext(request))

def success(request):
    return render_to_response("payments/success.html", {}, context_instance=RequestContext(request))
