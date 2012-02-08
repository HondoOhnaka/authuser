from django.conf.urls.defaults import patterns, include, url
from authuser.login_out import views
from django.contrib.auth.views import login, logout, logout_then_login

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.home),
    # url(r'^authuser/', include('authuser.foo.urls'))

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    (r'^accounts/login/$', login),
    (r'^login/$', login),
    (r'^accounts/login/$', login),
    (r'^logout/$', logout_then_login),
    (r'^login-required/$', views.login_req),
)
