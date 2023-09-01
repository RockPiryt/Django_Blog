from django.shortcuts import render

# Create your views here.

def index(request):
    render(request, "blog/index.html")

def posts(request):
    pass

def single_post(request):
    pass