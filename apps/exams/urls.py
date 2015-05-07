from django.conf.urls import patterns, include, url

from apps.exams import views

urlpatterns = patterns('',
                       url(r'^home/$', views.exam_list),
                       url(r'^(?P<test_id>\d+)/(?P<index>\d+)$',
                           views.get_question),
                       url(r'^(?P<test_id>\d+)/(?P<index>\d+)/save$',
                           views.save_answer),
                       url(r'^(?P<test_id>\d+)/result$', views.result),
                       )
