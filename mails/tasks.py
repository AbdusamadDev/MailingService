from celery import Celery

app = Celery('tasks', broker='pyamqp://guest:guest@localhost//')


@app.task
def schedule_send(instance, client, mail):
    print(instance, client, mail)
