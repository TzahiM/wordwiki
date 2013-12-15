# encoding: utf-8
from django.conf.urls import patterns, url
from pages import views


urlpatterns = patterns('',
    url(r'^$', views.list_of_all_pages, name='list_of_all_pages'),
    # ex: /word/hello/
    url(r'^(?P<pk>.+)/$', views.details, name='details'),
    # ex: /word/hello/edit
    url(r'^(?P<pk>.+)/edit$', views.PageUpdate.as_view(), name='edit'),
    # ex: /word/add
#    url(r'^add$', views.PageCreate.as_view(), name='create'),
)
