from django.contrib import admin
from music.models import Album

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('id', 'artist', 'album_title')
    list_display_links = ('id', 'artist')
    search_fields = ('album_title', 'artist')
    list_per_page = 25

admin.site.register(Album, AlbumAdmin)