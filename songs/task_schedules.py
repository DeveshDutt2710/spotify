from datetime import timedelta

song_schedules = {
    'calculate trending scores': {
        'task': 'songs.tasks.update_trending_scores',
        'schedule': timedelta(minutes=1),
    },
}
