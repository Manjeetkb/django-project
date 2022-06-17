from http.client import HTTPResponse
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')
    
def education(request):
    return render(request, 'education.html')

def research_lines(request):
    return render(request, 'research_lines.html')

def publications(request):
    return render(request, 'publications.html')

def extra(request):
    return render(request, 'extra.html')

def links(request):
    return render(request, 'links.html')