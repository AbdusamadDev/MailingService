from celery import shared_task

@shared_task
def your_task_function(instance):
    # Your logic here
    pass
