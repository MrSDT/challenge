from django.shortcuts import render
from django.shortcuts import HttpResponse

def about(request):
    return render(request, "about.html")

def home(request):
    return render(request, "home.html")

def required(request):
    return render(request, 'required.html')