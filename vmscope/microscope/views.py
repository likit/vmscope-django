from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import ParasiteImage, MicroscopeSection, Parasite

# Create your views here.
class ParasiteImageListView(ListView):
    model = ParasiteImage
    template_name = 'microscope/pr_image_list.html'
    context_object_name = 'images'


def parasite_report(request, pk):
    corrects = []
    incorrects = []
    scope_section = get_object_or_404(MicroscopeSection, pk=int(pk))
    parasites = Parasite.objects.all()
    if request.method == 'POST':
        answers = set(request.POST.getlist('answers'))
        parasite_components = []
        for item in scope_section.parasite_components.all():
            if str(item.parasite.id) in answers:
                corrects.append(str(item.parasite))
            else:
                incorrects.append(str(item.parasite))
    return render(request, 'microscope/parasite_report.html',
                  {'parasites': parasites,
                   'scope_section': scope_section,
                   'corrects': corrects,
                   'incorrects': incorrects,
                   })


class MicroscopeView(DetailView):
    model = MicroscopeSection
    template_name = 'microscope/microscope.html'
    context_object_name = 'scope'