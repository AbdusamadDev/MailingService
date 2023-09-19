from celery import Celery
import datetime

app = Celery('tasks', broker='redis://127.0.0.1:12345/0')

@app.task
def trigger_task():
    print("Trigger task called!")
    # Schedule another task to run after this
    scheduled_task.apply_async(eta=datetime.datetime.now() + datetime.timedelta(seconds=10))

@app.task
def scheduled_task():
    print("Scheduled task executed!")
