from celery import shared_task
from songs.models import Song
from songs.utils.trending_score import TrendingScoreCalculator
from django.core.cache import cache
from base.choices import BaseChoices
from songs.choices import GENRE_TYPE_CHOICES

@shared_task
def update_trending_scores():
    scorer = TrendingScoreCalculator()
    songs = Song.objects.all()

    for song in songs:
        song.trending_score = scorer.compute_score(song)
        song.save(update_fields=["trending_score"])

    top_100 = list(songs.order_by("-trending_score")[:100].values())
    cache.set("trending:all", top_100, timeout=None)

    genres = songs.values_list("genre", flat=True).distinct()
    for genre in genres:
        top_by_genre = list(
            songs.filter(genre=genre).order_by("-trending_score")[:100].values()
        )
        genre_name = BaseChoices().get_choice_str(GENRE_TYPE_CHOICES, genre).lower()
        cache.set(f"trending:genre:{genre_name}", top_by_genre, timeout=None)
