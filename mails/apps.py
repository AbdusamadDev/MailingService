from django.apps import AppConfig


class MailsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "mails"

    def ready(self):
        import mails.signals  # Importing signals.py here
        import mails.tasks