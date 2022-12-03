from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    return HttpResponse('<h1>Hallo to me</h1>')


def home(request):
    return render(request, 'moon/home.html')

def about(request):
    template = loader.get_template('moon/about.html')
    return HttpResponse(template.render())
