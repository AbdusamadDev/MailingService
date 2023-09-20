from rest_framework import serializers
from rest_framework.exceptions import ValidationError

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

    def validate(self, attrs):
        print(attrs.get("start_date"))
        print(attrs.get("end_date"))
        if attrs.get("start_date") > attrs.get("end_date"):
            raise ValidationError("Impossible datetime entered!")
        return attrs


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

    # def validate(self, attrs):
    #     if attrs.get("start_date") > attrs.get("end_date"):
    #         raise ValidationError("Impossible datetime entered!")
    #     return attrs


#
class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"
