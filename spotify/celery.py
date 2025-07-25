import os
from celery import Celery

from songs.task_schedules import song_schedules

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'spotify.settings')

app = Celery('spotify')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

scheduled_tasks = dict()

scheduled_tasks.update(song_schedules)
app.conf.beat_schedule = scheduled_tasks
