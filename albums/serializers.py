from rest_framework import serializers
from songs.serializers import SongSerializer
from .models import Album



class AlbumSerializer(serializers.ModelSerializer):
    songs = SongSerializer(many=True,read_only=True)

    class Meta:
        model = Album
        fields = ['id', 'name', 'musician_id','total_duration','songs','songs_count']
        read_only_fields = ['total_duration']
    total_duration = serializers.SerializerMethodField()
    songs_count = serializers.SerializerMethodField()

    def get_total_duration(self, album):
        songs = album.songs.all()
        total_duration = 0
        for song in songs:
            total_duration += song.duration
        return total_duration

    def get_songs_count(self, album):
        return album.songs.all().count()

    def create(self, validated_data):
        return Album.objects.create(**validated_data)
