from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from apps.api import views
from apps.api.views import QuestionViewSet

urlpatterns = patterns('',
                       url(r'^questions/$', QuestionList.as_view(),
                           name="question_list"),
                       url(r'^questions/(?P<question_id>\d+)/$',
                           views.question_details, name="question_details"),
                       url(r'^exams/$', views.exam_list, name='exam_list'),
                       url(r'^exams/(?P<exam_id>\d+)/$',
                           views.exam_detail, name='exam_detail'),
                       url(r'^tests/$', views.test_list, name='test_list'),

                       )

urlpatterns = format_suffix_patterns(urlpatterns)
