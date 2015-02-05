from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'diskdelivery.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'login/','django.contrib.auth.views.login',{"template_name":"login.html"},name='login'),
    url(r'logout/','django.contrib.auth.views.logout_then_login',{'login_url': '/'},name='logout'),

    url(r'^$', 'diskdelivery.core.views.inicio_site', name='inicio_site'),
    url(r'^home/$', 'diskdelivery.core.views.home', name='home'),
)
