from django.urls import path

from .views import MicroscopeSectionListView, MicroscopeSectionDetailView


urlpatterns = [
    path('microscope/', MicroscopeSectionListView.as_view()),
    path('microscope/<int:pk>', MicroscopeSectionDetailView.as_view()),
]