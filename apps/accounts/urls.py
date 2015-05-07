from django.conf.urls import patterns, include, url
from apps.accounts import views
urlpatterns = patterns('',
                       url(r'^$', 'django.contrib.auth.views.login'),
                       url(r'^logout/$', views.logout_page),
                       # If user is not login it will redirect to login page
                       url(r'^login/$', 'django.contrib.auth.views.login'),
                       url(r'^register/$', views.register),
                       url(r'^register/success/$', views.register_success),
                       url(r'^home/$', views.home),
                       )
