from django.urls import path

from .views import ParasiteImageListView, MicroscopeView, parasite_report


urlpatterns = [
    path('section/<int:pk>', MicroscopeView.as_view(), name='microscope'),
    path('images/', ParasiteImageListView.as_view(), name='image_list'),
    path('parasite_report/<int:pk>', parasite_report, name='parasite_report')
]