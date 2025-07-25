from django.utils import timezone
from songs.constants import TrendingScoreConstants

class TrendingScoreCalculator:
    def compute_score(self, song):
        now = timezone.now()
        recency_score = 1 / max((now - song.last_played).days + 1, 1)

        return (
            TrendingScoreConstants.PLAY_COUNT * song.play_count +
            TrendingScoreConstants.RECENCY * recency_score +
            TrendingScoreConstants.USER_RATING * song.user_rating +
            TrendingScoreConstants.SOCIAL_SHARES * song.social_shares +
            TrendingScoreConstants.GEO_POPULARITY * sum(song.geographic_popularity.values()) / 100
        )