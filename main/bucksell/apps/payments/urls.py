from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('payments.views',

    url(r'^cancel/$','cancelled',{},name = "payment_cancel"),
    url(r'^success/$','success',{},name = "payment_success"),

)
