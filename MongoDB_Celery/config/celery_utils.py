from celery import Celery

def create_celery():
    app = Celery('myapp', broker='redis://localhost:6379/0',backend='redis://localhost:6379/0')
    return app
