from songs.models import Song
from songs.utils.trending_score import TrendingScoreCalculator
from django.core.cache import cache
from base.choices import BaseChoices
from songs.choices import GENRE_TYPE_CHOICES, GenreTypes

class SongServiceHandler:
    def __init__(self):
        self.scorer = TrendingScoreCalculator()

    def generate_song_response(self, song):
        if isinstance(song, dict):
            genre = BaseChoices().get_choice_str(GENRE_TYPE_CHOICES, song['genre'])
            return {
                'uuid': song.get('uuid'),
                'title': song.get('title'),
                'artist': song.get('artist'),
                'album': song.get('album'),
                'genre': genre,
                'play_count': song.get('play_count'),
                'user_rating': song.get('user_rating'),
                'social_shares': song.get('social_shares'),
                'geographic_popularity': song.get('geographic_popularity'),
                'last_played': song.get('last_played'),
                'trending_score': song.get('trending_score')
            }
        else:
            return {
                'uuid': song.uuid,
                'title': song.title,
                'artist': song.artist,
                'album': song.album,
                'genre': BaseChoices().get_choice_str(song.genre),
                'play_count': song.play_count,
                'user_rating': song.user_rating,
                'social_shares': song.social_shares,
                'geographic_popularity': song.geographic_popularity,
                'last_played': song.last_played,
                'trending_score': song.trending_score
            }


    def get_trending_songs(self, genre=None):
        if genre:
            cache_key = f"trending:genre:{genre.lower()}"
        else:
            cache_key = "trending:all"

        cached_songs = cache.get(cache_key)
        if cached_songs:
            return [self.generate_song_response(song) for song in cached_songs]

        songs = Song.objects.all()
        if genre:
            try:
                genre_value = BaseChoices().get_choice_value(genre.upper())
                songs = songs.filter(genre=genre_value)
            except KeyError:
                return []

        songs = songs.order_by("-trending_score")[:100]
        song_dicts = list(songs.values())
        cache.set(cache_key, song_dicts, timeout=3600)

        return [self.generate_song_response(song) for song in song_dicts]

    
    def get_trending_songs_by_genre(self, genre):
        return self.get_trending_songs(genre)