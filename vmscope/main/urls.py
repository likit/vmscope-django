from django.urls import path

from .views import (IndexPageView, ProgramPageView,
                        SessionPageView, DisciplinePageView)

urlpatterns = [
    path('session/<int:pk>', SessionPageView.as_view(), name='session'),
    path('program/<int:pk>/', ProgramPageView.as_view(), name='program'),
    path('discipline/<int:pk>/', DisciplinePageView.as_view(), name='discipline'),
    path('', IndexPageView.as_view(), name='index'),
]
