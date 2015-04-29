from django.conf.urls import patterns, include, url
from django.contrib import admin
from apps.accounts import views

urlpatterns = patterns('',
                       url(r'^$', views.register),
                       url(r'^api/', include('apps.api.urls')),
                       url(r'^questions/', include('apps.questions.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^accounts/', include('apps.accounts.urls')),
                       url(r'^exams/', include('apps.exams.urls')),
                       )
