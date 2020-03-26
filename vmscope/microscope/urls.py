from django.urls import path

from .views import (ParasiteImageListView,
                    display_microscope_section,
                    parasite_report
                    )


urlpatterns = [
    path('section/<int:pk>', display_microscope_section, name='microscope'),
    path('images/', ParasiteImageListView.as_view(), name='image_list'),
    path('parasite_report/<int:pk>/<int:record_pk>', parasite_report, name='parasite_report')
]