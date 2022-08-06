import logging

from celery import Celery

# from settings.backend_setup import backend_manager

app = Celery('tasks', broker='amqp://')


@app.task()
def my_task(self, *args, **kwargs):
    # backend_manager.run_general_parsing()

    logging.debug('CELERY HERE')
