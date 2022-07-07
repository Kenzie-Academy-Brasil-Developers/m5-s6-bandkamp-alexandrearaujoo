from albums.serializers import AlbumSerializer
from rest_framework import serializers

from .models import Musician


class MusicianSerializer(serializers.ModelSerializer):
    albums = AlbumSerializer(many=True, read_only=True)

    class Meta:
        model = Musician
        fields = '__all__'


