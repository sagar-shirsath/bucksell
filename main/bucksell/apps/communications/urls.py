from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('communications.views',
    url(r'^$','index',{},name="message_index"),
    url(r'^add/$','add',{},name="message_add"),
    url(r'^reply/$','reply',{},name="message_reply"),
    url(r'^delete/(\d+)/*','delete',{},name="message_delete"),
#    url(r'^user_type/$','user_type',{},name = "user_profile_user_type"),

)
