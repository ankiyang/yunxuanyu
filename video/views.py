from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'video/index.html')


def video(request):
    return render(request, 'video/video.html')