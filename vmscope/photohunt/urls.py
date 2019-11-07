from django.urls import path

from .views import ImageListView


urlpatterns = [
    # path('section/<int:pk>', MicroscopeView.as_view(), name='microscope'),
    path('images/', ImageListView.as_view(), name='image_list'),
    # path('parasite_report/<int:pk>', parasite_report, name='parasite_report')
]