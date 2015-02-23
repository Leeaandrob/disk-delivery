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
    url(r'^carregar/$', 'diskdelivery.core.views.carregar', name='carregar'),
    url(r'^home/$', 'diskdelivery.core.views.home', name='home'),


    url(r'^comidas/',include('diskdelivery.comidas.urls',namespace='comidas')),
    url(r'^cardapios/',include('diskdelivery.cardapios.urls',namespace='cardapios')),
    url(r'^restaurantes/',include('diskdelivery.restaurantes.urls',namespace='restaurantes')),

    url(r'^clientes/',include('diskdelivery.clientes.urls',namespace='clientes')),
    url(r'^cadastro/$', 'diskdelivery.clientes.views.cadastro', name='cadastro'),
)
