from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now

from mails.models import Mails
from mails.tasks import your_task_function


@receiver(post_save, sender=Mails)
def schedule_celery_task(sender, instance, created, **kwargs):
    if created:  # only for newly created objects
        if instance.start_time > now():  # ensuring the start_time is in the future
            your_task_function.apply_async(args=[instance], eta=instance.start_time)
