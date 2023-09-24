from django.db.models import Q

from celery import shared_task
import requests
from dotenv import load_dotenv
import os

from mails.models import Message, Client, Mails

load_dotenv()


@shared_task(bind=True)
def schedule_send(self, json_data, mail_id, client_id):
    print("Json: ", json_data)
    url = os.getenv("URL")
    token = os.getenv("TOKEN")
    try:
        headers = {"Authorization": "Bearer %s" % (token,)}
        request = requests.post(
            f"{url}{json_data.get('id')}",
            json=json_data,
            headers=headers,
        )
        message = Message.objects.filter(pk=int(json_data.get("id")))
        print(int(client_id))
        print(type(int(client_id)))
        print(message)
        if message.exists():
            print("message does exist")
            message.update(status="Sent")

    except Exception as e:
        return "Task has completed with errors!\n{}".format(e)
