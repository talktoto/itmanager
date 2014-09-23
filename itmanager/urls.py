from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'itmanager.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^info/$', 'info.view.index'),
    url(r'index.html','itmanager.view.index'),
    url(r'^info/serverlist/','info.serverfrom.serverlist'),
    url(r'^reguser/$','info.index.userfrom'),
    url(r'^login/$','info.index.login'),
    url(r'^logout/$','info.index.logout'),
    url(r'^in/$','info.index.in1'),
    url(r'^showlogs/$','info.showlogs.showlog'),
    url(r'^showlogs/project','info.showlogs.project'),
)


