from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Discipline, Program, Session
from photohunt.models import Discipline as PhotohuntDiscipline
from django.contrib.auth.mixins import LoginRequiredMixin



def index(request):
    vmscope_dcps = list(Discipline.objects.all())
    photohunt_dcps = list(PhotohuntDiscipline.objects.all())
    template_name = 'main/index.html'
    context_object_name = 'discipline_list'
    return render(request, 'main/index.html',
                  {'vmscope_dcps': vmscope_dcps,
                   'photohunt_dcps': photohunt_dcps})


class DisciplinePageView(LoginRequiredMixin, DetailView):
    model = Discipline
    context_object_name = 'discipline'
    template_name = 'main/discipline.html'


class ProgramPageView(LoginRequiredMixin, DetailView):
    model = Program
    context_object_name = 'program'
    template_name = 'main/program.html'


class SessionPageView(LoginRequiredMixin, DetailView):
    model = Session
    context_object_name = 'session'
    template_name = 'main/session.html'
