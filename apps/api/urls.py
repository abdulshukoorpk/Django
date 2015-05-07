from django.conf.urls import patterns, url, include

from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

from apps.api import views

router = routers.SimpleRouter()
router.register(r'exams', views.ExamViewSet)
router.register(r'tests', views.TestViewSet)
exams_router = routers.NestedSimpleRouter(router, r'exams', lookup='exams')
exams_router.register(r'questions', views.QuestionViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^', include(exams_router.urls)),
    # url(r'^', include(tests_router.urls)),
    )
