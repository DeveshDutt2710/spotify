from django.contrib import admin
from songs.models import Song
from base.admin import BaseModelAdmin

# Register your models here.


@admin.register(Song)
class BankBrandAdmin(BaseModelAdmin):
    search_fields = ('uuid', 'title', 'album', 'artist', )
    list_display = ('uuid', 'title', 'album', 'artist', 'trending_score',
                    'genre', 'play_count', 'user_rating', 
                    'social_shares', 'geographic_popularity', 'last_played')