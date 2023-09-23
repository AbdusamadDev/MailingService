# tasks.py
from celery import shared_task
import logging

logger = logging.getLogger(__name__)

@shared_task
def schedule_send(instance, client, mail):
    print(instance, client, mail)
    logger.info("Executing task: %s %s %s", instance, client, mail)
