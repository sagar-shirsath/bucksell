from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('feedbacks.views',

    url(r'^all/','feedbacks',{},name = "feedbacks"),
    url(r'^add','add',{},name = "feedbacks_add"),

    
)
