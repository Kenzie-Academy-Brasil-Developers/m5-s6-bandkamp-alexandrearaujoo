from albums.models import Album
from albums.serializers import AlbumSerializer
from django.shortcuts import get_object_or_404

from songs.models import Song
from songs.serializers import SongSerializer
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from .models import Musician
from .serializers import MusicianSerializer

class ListCreateView(generics.ListCreateAPIView):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer
    pagination_class = PageNumberPagination

class RetriveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer


class ListCreateMusicianAlbumView(generics.ListCreateAPIView):
    serializer_class = AlbumSerializer
    pagination_class = PageNumberPagination

    def perform_create(self, serializer):
        musician = get_object_or_404(Musician, pk=self.kwargs['pk'])

        serializer.save(musician=musician)

    def get_queryset(self):
        musician = get_object_or_404(Musician, pk=self.kwargs['pk'])

        return Album.objects.filter(musician=musician)

class ListCreateMusicianAlbumSongView(generics.ListCreateAPIView):
    serializer_class = SongSerializer
    pagination_class = PageNumberPagination

    def perform_create(self, serializer):
        musician = get_object_or_404(Musician, pk=self.kwargs['pk'])
        album = Album.objects.filter(musician=musician, id=self.kwargs['album_id']).first()

        serializer.save(album=album)

    def get_queryset(self):
        musician = get_object_or_404(Musician, pk=self.kwargs['pk'])
        album = get_object_or_404(Album, pk=self.kwargs['album_id'])

        songs = Song.objects.filter(musician=musician, album=album)

        return songs
        
