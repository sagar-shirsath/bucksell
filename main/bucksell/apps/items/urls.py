from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('items.views',
    url(r'browse/','index',{},name = "item_index"),
    url(r'add/','add',{},name = "add_item"),
    url(r'my_shop/','my_listing',{},name = "my_listing"),
    url(r'edit/(?P<slug>[-\w\d]+)','edit',{},name = "item_edit"),
    url(r'view/(?P<slug>[-\w\d]+)','view',{},name = "item_view"),
    url(r'delete/(?P<slug>[-\w\d]+)','delete',{},name = "item_delete"),
    url(r'view_item_ajax/(?P<id>[\d]+)','view_item_ajax',{},name = "view_item_ajax"),
    url(r'search/','search',{},name = "search"),
    url(r'publish/','publish',{},name = "item_publish"),
#    url(r'^user_type/$','user_type',{},name = "user_profile_user_type"),
    
)
