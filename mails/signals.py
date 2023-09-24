# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.utils.timezone import now
# from django.db.models import Q

# from datetime import timedelta, datetime
# from mails.models import Mails, Client, Message
# from mails.tasks import schedule_send

# import logging

# logger = logging.getLogger(__name__)


# @receiver(post_save, sender=Mails)
# def handle_creation(sender, instance, created, **kwargs):
#     if created:  # only for newly created objects
#         clients = Client.objects.filter(
#             Q(phone_number=instance.client_phone_code) | Q(tag=instance.client_tag)
#         )
#         print(type(instance.start_date))
#         logger.info(f"Scheduling mail with id {instance.id} for {instance.start_date}")
#         for client in clients:
#             """
#             Here Message object is the connection between mails and clients
#             It judges which mails should be sent to which client and the amount
#             of messages
#             """
#             message = Message.objects.create(client=client, mail=instance)
#             json_data = {
#                 "id": message.id,
#                 "text": instance.body,
#                 "phone": client.phone_number,
#             }
#             print("Datetime: ", instance.start_date < now() < instance.end_date)
#             print(instance.start_date)
#             print(now())
#             print(instance.end_date)
#             result = schedule_send.apply_async(
#                 args=[json_data, client.id, instance.id],
#                 eta=datetime.now() + timedelta(seconds=5),
#             )

#             # if (
#             #     instance.start_date <= now() <= instance.end_date
#             # ):  # checking if it's time to send
#             #     """
#             #     The `if` condition is defined to prevent if for some reason
#             #     data will be created right at the same time that should be sent
#             #     """
#             #     print("It is time to send")
#             #     result = schedule_send.apply_async(
#             #         args=[json_data, client.id, instance.id],
#             #         expires=instance.end_date,
#             #     )
#             #     # print(result.result)
#             # elif (
#             #     instance.start_date > now() and instance.end_date > instance.start_date
#             # ):  # checking both start and end time hasn't come yet
#             #     print("It is scheduled")
#             #     result = schedule_send.apply_async(
#             #         args=[json_data, client.id, instance.id],
#             #         eta=instance.start_date,
#             #         expires=instance.end_date,
#             #     )
#             #     # print(result.result)
