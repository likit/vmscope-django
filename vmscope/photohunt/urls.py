from django.urls import path

from .views import ImageListView, ImageView


urlpatterns = [
    path('image_view/<int:pk>', ImageView.as_view(), name='image_view'),
    path('images/', ImageListView.as_view(), name='image_list'),
    # path('parasite_report/<int:pk>', parasite_report, name='parasite_report')
]