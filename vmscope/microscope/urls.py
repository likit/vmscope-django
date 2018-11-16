from django.urls import path

from .views import ParasiteImageListView, MicroscopeView


urlpatterns = [
    path('section/<int:pk>', MicroscopeView.as_view(), name='microscope'),
    path('images/', ParasiteImageListView.as_view(), name='image_list')
]