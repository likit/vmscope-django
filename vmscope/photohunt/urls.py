from django.urls import path

from .views import (ImageListView, ImageView,
                    DisciplinePageView, ProgramPageView,
                    show_session, show_tagset,)

app_name = "photohunt"

urlpatterns = [
    path('discipline/<int:pk>', DisciplinePageView.as_view(), name='show_discipline'),
    path('program/<int:pk>', ProgramPageView.as_view(), name='show_program'),
    path('session/<int:pk>', show_session, name='show_session'),
    path('session/<int:session_pk>/tagset/<int:tsnum>', show_tagset, name='show_tagset'),
    path('image_view/<int:pk>', ImageView.as_view(), name='image_view'),
    path('images/', ImageListView.as_view(), name='image_list'),
    # path('parasite_report/<int:pk>', parasite_report, name='parasite_report')
]