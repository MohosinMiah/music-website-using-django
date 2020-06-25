from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the Blogs index.")



# def detail(request,album_id):
#     return HttpResponse("Album Details")

def detail(request, album_id):
    response = "You're looking at the details results of Album  %s."
    return HttpResponse(response % album_id)