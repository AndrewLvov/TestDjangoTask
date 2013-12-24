from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^api/get_users/', 'employees.views.get_users', name='get_users'),
    url(r'^api/get_user/', 'employees.views.get_user', name='get_user'),

    url(r'^admin/', include(admin.site.urls)),
)
