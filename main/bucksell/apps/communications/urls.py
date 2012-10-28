from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('communications.views',

    url(r'^add/','add',{},name="message_add"),
    url(r'^','index',{},name="message_index"),
#    url(r'^user_type/$','user_type',{},name = "user_profile_user_type"),

)
