from celery import Celery

# Create a Celery app
app = Celery('myapp', broker='redis://localhost:6379/0',backend='redis://localhost:6379/0')  # Use a broker like Redis to handle task messages

# Define a Celery task
@app.task
def add(x, y):
    return x + y
