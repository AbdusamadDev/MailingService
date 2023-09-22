from celery import shared_task

@shared_task
def schedule_send(instance):
    # Your logic here
    pass
