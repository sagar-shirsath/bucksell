from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('items.views',
    url(r'browse/','index',{},name = "item_index"),
    url(r'add/','add',{},name = "add_item"),
#    url(r'^user_type/$','user_type',{},name = "user_profile_user_type"),
    
)
