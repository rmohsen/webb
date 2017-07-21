import celery
import os
from django.conf import settings

app = celery.Celery('example')

app.conf.update(BROKER_URL=os.environ['REDIS_URL'],
                CELERY_RESULT_BACKEND=os.environ['REDIS_URL'])

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task
def add(x,y):
    return x+y
