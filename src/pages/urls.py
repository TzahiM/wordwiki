from django.conf.urls import patterns, url

from pages import views

urlpatterns = patterns('',
    url(r'^$', views.list_of_all_pages, name='list_of_all_pages'),
)
