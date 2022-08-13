import logging

from celery import Celery

from kombu import Exchange, Queue

# from .backend.backend_manager import BackendManager


class Config(object):
    CELERY_QUEUES = (
        Queue(
            'main_queue',
            exchange=Exchange('main_queue'),
            routing_key='main_queue',
        ),
    )


celery_app = Celery('tasks', broker='pyamqp://guest@localhost//')

celery_app.config_from_object(Config)


celery_app.conf.beat_schedule = {
    'planner': {
        'task': 'tasks.run_parsing',
        # 'schedule': 43200.0,
        'schedule': 5,
    },
}


@celery_app.task(queue='main_queue')
def run_parsing():
    # backend_manager = BackendManager()
    # backend_manager.run_general_parsing()
    logging.info('Run parsing')
