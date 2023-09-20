from django.db import models
import pytz as timezone


# Status of mailings
CHOICES = (("Sent", "Not Sent"), ("Sent", "Not Sent"))


class Client(models.Model):
    TIMEZONE_CHOICES = [(tz, tz) for tz in timezone.all_timezones]
    username = models.CharField(max_length=150, null=False, unique=True, blank=False)
    email = models.EmailField(max_length=250, null=False, unique=True, blank=False)
    tag = models.CharField(max_length=50, null=False, blank=False, unique=False)
    phone_number = models.IntegerField(null=False, unique=False, blank=False)
    timezone = models.CharField(max_length=63, choices=TIMEZONE_CHOICES, default="UTC")
    # Django uses timezone by default
    date_joined = models.DateTimeField(auto_now_add=True)


class Mails(models.Model):
    client_phone_code = models.CharField(
        max_length=30, null=False, unique=False, blank=False
    )
    client_tag = models.CharField(max_length=50, unique=False, blank=False, null=False)
    body = models.TextField(max_length=5000, blank=False, null=False, unique=False)
    # Extra field for classify mails with their sending status
    status = models.CharField(max_length=15, choices=CHOICES, default="Not Sent")
    start_date = models.DateTimeField(null=False, blank=False)
    end_date = models.DateTimeField(null=False, blank=False)

    class Meta:
        """
        Database indexing is vital for optimizing filtering operations,
        especially with large datasets. By creating an index on specific
        columns, the database can quickly identify and retrieve the desired rows,
        significantly enhancing the efficiency and speed of filter-based queries

        Based on task, those two fields are being filtered here.
        """

        ordering = ["pk"]
        indexes = [
            models.Index(
                fields=["client_phone_code", "client_tag"], name="filter_indexes"
            )
        ]


class Message(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    mail = models.ForeignKey(Mails, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20,
        choices=CHOICES,
        default="Not Sent",
        blank=False,
        unique=False,
        null=False,
    )
    sent_at = models.DateTimeField(null=True, blank=True)
