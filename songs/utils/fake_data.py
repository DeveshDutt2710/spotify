import random
from faker import Faker
from django.utils import timezone
from songs.models import Song
from songs.choices import GENRE_TYPE_CHOICES
from base.choices import BaseChoices

fake = Faker()

def create_fake_songs(n=500):
    genres = BaseChoices().get_full_choice_string_list(GENRE_TYPE_CHOICES)
    for _ in range(n):
        Song.objects.create(
            uuid=fake.uuid4(),
            title=fake.sentence(nb_words=3),
            artist=fake.name(),
            album=fake.word(),
            genre=BaseChoices.get_choice_value(GENRE_TYPE_CHOICES, random.choice(genres)),
            play_count=random.randint(100, 100000),
            user_rating=round(random.uniform(1.0, 5.0), 1),
            social_shares=random.randint(0, 10000),
            geographic_popularity={
                'US': random.randint(0, 100),
                'IN': random.randint(0, 100),
                'UK': random.randint(0, 100),
            },
            last_played=timezone.now() - timezone.timedelta(days=random.randint(0, 30))
        )
