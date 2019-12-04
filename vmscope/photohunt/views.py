from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Image, Session

class ImageListView(ListView):
    model = Image
    template_name = 'photohunt/image_list.html'
    context_object_name = 'images'


class ImageView(DetailView):
    model = Image
    template_name = 'photohunt/coord_set.html'
    context_object_name = 'image'


class SessionView(ListView):
    model = Session
    template_name = 'photohunt/index.html'
    context_object_name = 'sessions'


def show_session(request, pk):
    session = get_object_or_404(Session, pk=pk)
    return render(request,
                  'photohunt/session.html',
                  {'session': session})
