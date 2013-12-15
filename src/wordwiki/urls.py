from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from pages import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wordwiki.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^word/', include('pages.urls', namespace="pages")),
    url(r'^add-word/$', views.PageCreate.as_view(), name="create"),
    url(r'^admin/', include(admin.site.urls)),
)

