from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('hello world')


def about(request):
    return HttpResponse('about page')


def services(request):
    return HttpResponse('services page')


def store(request):
    return HttpResponse('store pages')


def contact(request):
    return HttpResponse('contact page')


def blog(request):
    return HttpResponse('blog page')


def sample(request):
    return HttpResponse('sample page')