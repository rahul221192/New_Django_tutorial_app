from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name='home/home.html'