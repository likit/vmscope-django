from django.urls import path

from .views import ImageListView, ImageView, SessionView, show_session


urlpatterns = [
    path('session/<int:pk>', show_session, name='show_session'),
    path('session/', SessionView.as_view(), name='session_list'),
    path('image_view/<int:pk>', ImageView.as_view(), name='image_view'),
    path('images/', ImageListView.as_view(), name='image_list'),
    # path('parasite_report/<int:pk>', parasite_report, name='parasite_report')
]