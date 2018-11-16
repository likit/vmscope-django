from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import ParasiteImage, MicroscopeSection

# Create your views here.
class ParasiteImageListView(ListView):
    model = ParasiteImage
    template_name = 'microscope/pr_image_list.html'
    context_object_name = 'images'


class MicroscopeView(DetailView):
    model = MicroscopeSection
    template_name = 'microscope/microscope.html'
    context_object_name = 'scope'