from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'gdgjalandhar.views.home', name='home'),
    url(r'^about/', 'gdgjalandhar.views.about', name='about'),
    url(r'^events/', 'gdgjalandhar.views.events', name='events'),
    url(r'^gallery/', 'gdgjalandhar.views.gallery', name='gallery'),
    url(r'^contactus/', 'gdgjalandhar.views.contactus', name='contactus'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
