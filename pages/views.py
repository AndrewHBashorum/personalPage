from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'pages/home.html')

def lanu(request):
    return render(request, 'pages/lanu.html')

def blog(request):
    return render(request, 'pages/blog.html')

def youtube(request):
    return render(request, 'pages/youtube.html')

def gallery(request):
    return render(request, 'pages/gallery.html')

def models(request):
    return render(request, 'pages/models.html')

def research(request):
    return render(request, 'pages/research.html')
