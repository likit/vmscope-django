from django.urls import path

from .views import (MicroscopeSectionListView, MicroscopeSectionDetailView,
                    ParasiteComponentDetailView)


urlpatterns = [
    path('microscope/', MicroscopeSectionListView.as_view()),
    path('microscope/<int:pk>', MicroscopeSectionDetailView.as_view()),
    path('microscope/component/<int:pk>', ParasiteComponentDetailView.as_view()),
]