from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import (ParasiteImage, MicroscopeSection,
                     Parasite, MicroscopePlayRecord)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class ParasiteImageListView(LoginRequiredMixin, ListView):
    model = ParasiteImage
    template_name = 'microscope/pr_image_list.html'
    context_object_name = 'images'


@login_required
def parasite_report(request, pk, record_pk):
    corrects = []
    incorrects = []
    missing = []
    scope_section = get_object_or_404(MicroscopeSection, pk=int(pk))
    record = get_object_or_404(MicroscopePlayRecord, pk=int(record_pk))
    parasites = Parasite.objects.all()
    parasite_components = []
    if request.method == 'POST':
        answers = set(request.POST.getlist('answers'))
        for item in scope_section.parasite_components.all():
            if str(item.parasite.id) in answers:
                corrects.append(str(item.parasite))
            else:
                missing.append(str(item.parasite))
            parasite_components.append(item)
        all_parasite_comp_ids = set([item.parasite.id for
                                     item in scope_section.parasite_components.all()])
        for ans in answers:
            p = get_object_or_404(Parasite, pk=int(ans))
            if p.id not in all_parasite_comp_ids:
                incorrects.append(str(p))

        record.score = len(corrects) - (len(incorrects) + len(missing))
        record.saved_at = timezone.now()
        record.save()
        print(record.saved_at, record.score)
    return render(request, 'microscope/parasite_report.html',
                  {'parasites': parasites,
                   'scope_section': scope_section,
                   'corrects': corrects,
                   'incorrects': incorrects,
                   'missing': missing,
                   'parasite_components': parasite_components,
                   })

@login_required
def display_microscope_section(request, pk):
    scope_section = get_object_or_404(MicroscopeSection, pk=int(pk))
    record = MicroscopePlayRecord(section=scope_section, user=request.user)
    record.save()
    return render(request, 'microscope/microscope.html',
                  {'scope': scope_section,
                   'record': record}
                  )
