from celery import shared_task

@shared_task(bind=True)
def schedule_send(self):
    # Task implementation here
    # print(instance)
    # print(client_id)
    # print(mail_id)
    return "Everything is okay, homie"

print("File is being run")