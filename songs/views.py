from rest_framework.views import APIView # type: ignore
from rest_framework.response import Response # type: ignore
from songs.handlers.song_service_handler import SongServiceHandler # type: ignore

class TrendingSongsAPIView(APIView):
    def get(self, request):
        response = SongServiceHandler().get_trending_songs()
        return Response({'songs': response})
    

class GenreTrendingSongsAPIView(APIView):
    def get(self, request, genre):
        response = SongServiceHandler().get_trending_songs_by_genre(genre)
        return Response({'songs': response})