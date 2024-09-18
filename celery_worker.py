from celery import Celery
from celery.schedules import crontab
from src import tasks

app = Celery('synergyway', include=['src.tasks'],
             broker='redis://redis:6379/0',
             backend='redis://redis:6379/0')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'fetch_users': {
        'task': 'fetch_users',
        'schedule': crontab(minute='*/10'),
    },
    'fetch_address': {
        'task': 'fetch_address',
        'schedule': crontab(minute='*/12'),
    },
    'fetch_card': {
        'task': 'fetch_cards',
        'schedule': crontab(minute='*/14'),
    },
}