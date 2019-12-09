from django.urls import path

from .views import (index, ProgramPageView,
                        SessionPageView, DisciplinePageView)

urlpatterns = [
    path('session/<int:pk>', SessionPageView.as_view(), name='session'),
    path('program/<int:pk>/', ProgramPageView.as_view(), name='program'),
    path('discipline/<int:pk>/', DisciplinePageView.as_view(), name='discipline'),
    path('', index, name='index'),
]
