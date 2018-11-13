from django.shortcuts import render
from django.views.generic import TemplateView


class IndexPageView(TemplateView):
    template_name = 'main/index.html'


class ProgramPageView(TemplateView):
    template_name = 'main/program.html'
