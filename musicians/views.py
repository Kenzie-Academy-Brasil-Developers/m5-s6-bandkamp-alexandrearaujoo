from albums.models import Album
from albums.serializers import AlbumSerializer
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Response, status
from songs.models import Song
from songs.serializers import SongSerializer
from rest_framework import generics

from .models import Musician
from .serializers import MusicianSerializer


def get_object_by_id(model, id):
        object = get_object_or_404(model, id=id)

        return object

# Create your views here.
class ListCreateView(generics.ListCreateAPIView):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer

class RetriveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer


class ListCreateMusicianAlbumView(generics.ListCreateAPIView):
    serializer_class = AlbumSerializer

    def perform_create(self, serializer):
        musician = get_object_or_404(Musician, pk=self.kwargs['pk'])

        serializer.save(musician=musician)

    def get_queryset(self):
        musician = get_object_or_404(Musician, pk=self.kwargs['pk'])

        return Album.objects.filter(musician=musician)

class MusicianAlbumSongView(APIView):
    def get(self, request, musician_id, album_id):
        musician = get_object_by_id(Musician ,musician_id)
        album = get_object_by_id(Album, album_id)
        songs = Song.objects.filter(musician=musician, album=album)

        serializer = SongSerializer(songs, many=True)

        return Response(serializer.data)

    def post(self, request, musician_id, album_id):
        musician = get_object_by_id(Musician, musician_id)

        album = Album.objects.filter(musician=musician, id=album_id).first()

        if not album:
            return Response({'detail': 'Album not Found'}, status.HTTP_404_NOT_FOUND)

        serializer = SongSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(album=album)

        return Response(serializer.data, status.HTTP_201_CREATED)
