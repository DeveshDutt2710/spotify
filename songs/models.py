from django.db import models # type: ignore
from base.models import AbstractBaseModel
from songs.choices import (
    GENRE_TYPE_CHOICES,
    GenreTypes
)

class Song(AbstractBaseModel):
    title = models.CharField(max_length=255, db_index=True)
    artist = models.CharField(max_length=255)
    album = models.CharField(max_length=255)
    genre = models.IntegerField(
        choices=GENRE_TYPE_CHOICES,
        default=GenreTypes.POP, db_index=True
    )
    play_count = models.PositiveIntegerField(default=0)
    user_rating = models.FloatField(default=0.0)
    social_shares = models.PositiveIntegerField(default=0)
    geographic_popularity = models.JSONField(default=dict)
    last_played = models.DateTimeField()
    trending_score = models.FloatField(default=0.0, db_index=True)