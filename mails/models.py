from django.db import models
import pytz as timezone


class Client(models.Model):
    TIMEZONE_CHOICES = [(tz, tz) for tz in timezone.all_timezones]
    username = models.CharField(max_length=150, null=False, unique=True, blank=False)
    email = models.EmailField(max_length=250, null=False, unique=True, blank=False)
    phone_number = models.IntegerField(null=False, unique=False, blank=False)
    timezone = models.CharField(max_length=63, choices=TIMEZONE_CHOICES, default="UTC")


class Mails(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    body = models.TextField()
    status = models.CharField(max_length=50, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)
    scheduled_at = models.DateTimeField(null=True, blank=True)
    sent_at = models.DateTimeField(null=True, blank=True)


# class Message(models.Model):
#     client = models.ForeignKey(Client, on_delete=models.CASCADE)
#     content = models.TextField()
#     sent_status = models.CharField(max_length=50, default="pending")
#     created_at = models.DateTimeField(auto_now_add=True)
#     sent_at = models.DateTimeField(null=True, blank=True)

