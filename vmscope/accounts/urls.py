from django.urls import path

from .views import SignUpView, update_profile

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('edit_profile/', update_profile, name='edit_profile')
]