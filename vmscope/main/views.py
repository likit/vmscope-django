from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Discipline, Program, Session


class IndexPageView(ListView):
    model = Discipline
    template_name = 'main/index.html'
    context_object_name = 'discipline_list'


class DisciplinePageView(DetailView):
    model = Discipline
    context_object_name = 'discipline'
    template_name = 'main/discipline.html'


class ProgramPageView(DetailView):
    model = Program
    context_object_name = 'program'
    template_name = 'main/program.html'


class SessionPageView(DetailView):
    model = Session
    context_object_name = 'session'
    template_name = 'main/session.html'
