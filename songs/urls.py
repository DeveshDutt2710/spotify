from django.urls import path # type: ignore
from songs.views import (
    TrendingSongsAPIView, 
    GenreTrendingSongsAPIView,
)
app_name = "songs"

urlpatterns = [
    path('trending-songs/', TrendingSongsAPIView.as_view(), name='trending-songs'),
    path('trending-songs/<str:genre>/', GenreTrendingSongsAPIView.as_view(), name='genre-trending-songs')
]