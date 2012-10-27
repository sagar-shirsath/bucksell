from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('items.views',
    url(r'browse/','index',{},name = "item_index"),
    url(r'add/','add',{},name = "add_item"),
    url(r'my_shop/','my_listing',{},name = "my_listing"),
    url(r'edit/(?P<slug>[-\w\d]+)','edit',{},name = "item_edit"),
    url(r'view/(?P<slug>[-\w\d]+)','view',{},name = "item_view"),
    url(r'search/','search',{},name = "search"),
#    url(r'^user_type/$','user_type',{},name = "user_profile_user_type"),
    
)
