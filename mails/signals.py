from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now
from django.db.models import Q

from mails.models import Mails, Client, Message
from mails.tasks import schedule_send

import pytz
import logging
from datetime import datetime

logger = logging.getLogger(__name__)


@receiver(post_save, sender=Mails)
def handle_creation(sender, instance, created, **kwargs):
    if created:  # only for newly created objects
        clients = Client.objects.filter(
            Q(phone_number=instance.client_phone_code) | Q(tag=instance.client_tag)
        )
        print(type(instance.start_date))
        logger.info(f"Scheduling mail with id {instance.id} for {instance.start_date}")
        for client in clients:
            """
            Here Message object is the connection between mails and clients
            It judges which mails should be sent to which client and the amount
            of messages
            """
            message = Message.objects.create(client=client, mail=instance)
            json_data = {
                "id": message.id,
                "text": instance.body,
                "phone": client.phone_number,
            }
            # json_data, client.id, instance.id
            timezone = pytz.timezone("Asia/Tashkent")
            desired_eta_local = timezone.localize(
                datetime.strptime(
                    str(instance.start_date).split("+")[0], "%Y-%m-%d %H:%M:%S"
                )
            )

            schedule_send.apply_async(args=[json_data], eta=desired_eta_local)
