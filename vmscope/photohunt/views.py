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


def show_tagset(request, session_pk, tsnum=0):
    if request.method == 'POST':
        for k,v in request.POST.items():
            if k.startswith('tag_'):
                request.session[k] = v
        curtag_num = int(request.POST.get('tsnum'))
        session_pk = int(request.POST.get('session_pk'))
        tsnum = curtag_num + 1

    session = get_object_or_404(Session, pk=session_pk)
    tagsets = session.tagsets.all()
    if tsnum >= len(tagsets):
        tagsets_results = {}
        for tagset in tagsets.all():
            reports = []
            for tag in tagset.tags.all():
                q = 'tag_{}'.format(tag.pk)
                a = request.session.get(q)
                res = True if a == tag.answer else False
                reports.append((tag, a, res))
            tagsets_results[tagset] = reports
        return render(request,
                      'photohunt/session_end.html',
                      {'results': tagsets_results,
                       'session': session})

    try:
        tagset = tagsets[tsnum]
    except IndexError:
        pass
    return render(request,
                  'photohunt/tagset.html',
                  {'session': session,
                   'tagset': tagset,
                   'tagset_number': tsnum})
