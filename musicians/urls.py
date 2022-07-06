from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

from . import views

urlpatterns = [
    path('musicians/', views.ListCreateView.as_view()),
    path('musicians/<pk>/', views.RetriveUpdateDeleteView.as_view()),
    path('musicians/<pk>/albums/', views.ListCreateMusicianAlbumView.as_view()),
    path('musicians/<pk>/albums/<str:album_id>/songs/', views.ListCreateMusicianAlbumSongView.as_view()),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
