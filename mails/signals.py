from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now
from django.db.models import Q

from mails.models import Mails, Client, Message
from mails.tasks import schedule_send


@receiver(post_save, sender=Mails)
def handle_creation(sender, instance, created, **kwargs):
    print("Function itself started")
    if created:  # only for newly created objects
        clients = Client.objects.filter(
            Q(phone_number=instance.client_phone_code) | Q(tag=instance.client_tag)
        )
        print("Instance: ", instance)
        print("Client: ", clients)
        print("Giving signal")
        if clients is not None:
            for client in clients:
                print("Client: ", client)
                """
                Here Message object is the connection between mails and clients
                It judges which mails should be sent to which client and the amount
                of messages
                """
                Message.objects.create(client=client, mail=instance.id)
                message = Message.objects.filter(
                    mailing_id=instance.id, client_id=client.id
                ).first()
                json_data = {
                    "id": message.id,
                    "text": instance.body,
                    "phone": client.phone_number,
                }
                if (
                    instance.start_date <= now() <= instance.end_date
                ):  # checking if it's time to send
                    """
                    The `if` condition is defined to prevent if for some reason
                    data will be created right at the same time that should be sent
                    """
                    schedule_send.apply_async(
                        args=[instance, json_data, client.id, instance.id],
                        expires=instance.end_date,
                    )
                elif (instance.start_date >= now()) and (
                    instance.end_date >= now()
                ):  # checking both start and end time hasn't come yet
                    schedule_send.apply_async(
                        args=[instance, json_data, client.id, instance.id],
                        eta=instance.start_date,
                        expires=instance.end_date,
                    )
