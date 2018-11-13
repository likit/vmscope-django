from django.urls import path

from .views import IndexPageView, ProgramPageView

urlpatterns = [
    path('program/', ProgramPageView.as_view(), name='program'),
    path('', IndexPageView.as_view(), name='index'),
]
