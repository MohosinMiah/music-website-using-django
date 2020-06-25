from django.shortcuts import render
from .models import Album,Song

# Create your views here.
from django.http import HttpResponse


def index(request):
    latest_album_list = Album.objects.all()
    hello = "Hello World! Pass Data to View for Display"
    context = {'latest_album_list': latest_album_list,'data': hello}
    return render(request, 'music/index.html', context)




# def detail(request,album_id):
#     return HttpResponse("Album Details")

def detail(request, album_id):
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
            raise Http404("Album does not exist")
    return render(request, 'music/detail.html', {'album': album})