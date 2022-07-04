from django.urls import path

from . import views

urlpatterns = [
    path('musicians/', views.ListCreateView.as_view()),
    path('musicians/<pk>/', views.RetriveUpdateDeleteView.as_view()),
    path('musicians/<pk>/albums/', views.ListCreateMusicianAlbumView.as_view()),
    path('musicians/<int:musician_id>/albums/<int:album_id>/songs/', views.MusicianAlbumSongView.as_view()),
]
