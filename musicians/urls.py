from django.urls import path

from . import views

urlpatterns = [
    path('musicians/', views.ListCreateView.as_view()),
    path('musicians/<pk>/', views.RetriveUpdateDeleteView.as_view()),
    path('musicians/<pk>/albums/', views.ListCreateMusicianAlbumView.as_view()),
    path('musicians/<pk>/albums/<int:album_id>/songs/', views.ListCreateMusicianAlbumSongView.as_view()),
]
