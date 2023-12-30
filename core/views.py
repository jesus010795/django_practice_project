from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(
        request, 
        template_name='core/home.html'
        )


def about(request):
    return render(
        request, 
        template_name='core/about.html'
        )


def store(request):
    return render(
        request, 
        template_name='core/store.html'
        )


def contact(request):
    return render(
        request, 
        template_name='core/contact.html'
        )
