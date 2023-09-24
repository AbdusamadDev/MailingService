from celery import shared_task
import requests


@shared_task(bind=True)
def schedule_send(self, json_data):
    
    return "Everything is okay, homie"

print("File is being run")