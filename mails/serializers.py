from rest_framework import serializers

from mails.models import Mails, Client, Message


class MailingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mails
        fields = [
            "id",
            "client_phone_code",
            "client_tag",
            "body",
            "start_date",
            "end_date",
        ]


class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"


class MessagesStatisticsSerializer(serializers.ModelSerializer):
    client = ClientsSerializer(read_only=True)
    mail = MailingSerializer(read_only=True)

    class Meta:
        model = Message
        fields = "__all__"

    def validate_start_date(self):
        pass
    

class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"
