
from rest_framework import serializers
import musicians
from musicians.models import Musician

from .models import Song


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id','name', 'duration','album_id', 'musician_id']

    musician_id = serializers.SerializerMethodField()

    def get_musician_id(self, song):
        musician = Musician.objects.get(albums=song.album_id)

        return musician.id

    def create(self, validated_data):
        return Song.objects.create(**validated_data)
