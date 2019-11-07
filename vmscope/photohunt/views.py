from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Image

class ImageListView(ListView):
    model = Image
    template_name = 'photohunt/image_list.html'
    context_object_name = 'images'


class ImageView(DetailView):
    model = Image
    template_name = 'photohunt/coord_set.html'
    context_object_name = 'image'