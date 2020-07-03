# from django.shortcuts import render,get_object_or_404
from .models import Album, Song
from django.urls import reverse_lazy
# from django.core.urlresolvers import reverse_lazy
# Create your views here
# from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView

class IndexView(ListView):

    template_name = "music/index.html"
    context_object_name = "latest_album_list"

    def get_queryset(self):
        return Album.objects.all()



class AlbumDetail(DetailView):

    model = Album

    context_object_name = "album_details"

    template_name= "music/detail.html"


class AlbumCreate(CreateView):
    model = Album
    fields = ['artist','album_title','genre','album_logo']


class AlbumCrete(CreateView):
    model = Album
    fields = ['artist','album_title','genre','album_logo']




class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist','album_title','genre','album_logo']
    template_name_suffix = '_update_form'




class AlbumDelete(DeleteView):
    model = Album
    # success_url = "/music/"
    success_url = reverse_lazy("music:index")







# def index(request):
#     latest_album_list = Album.objects.all()
#     hello = "Hello World! Pass Data to View for Display"
#     context = {'latest_album_list': latest_album_list,'data': hello}
#     return render(request, 'music/index.html', context)




# # def detail(request,album_id):
# #     return HttpResponse("Album Details")

# def detail(request, album_id):
#     try:
#         album_details = get_object_or_404(Album, pk=album_id)
#     except Album.DoesNotExist:
#         raise Http404("Album does not exist")
#     return render(request, 'music/detail.html', {'album_details': album_details},)




# def favorite(request,album_id):
#     album_details = get_object_or_404(Album, pk=album_id)
#     try:
#         selected_song = album_details.song_set.get(pk=request.POST['song'])
#     except (KeyError, Song.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'music/detail.html', {
#             'album_details': album_details,
#             'error_message': "You didn't select a song.",
#         })
#     else:
#         selected_song.is_favorite = True
#         selected_song.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('music:detail', args=(album_details.id,)))    