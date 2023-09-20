from rest_framework.pagination import PageNumberPagination
from rest_framework.status import HTTP_200_OK
from rest_framework.response import Response

from mails.models import Mails, Message, Client


class MailingPagination(PageNumberPagination):
    page_size = 5

    def get_pagated_response(self, data):
        # This is the original structure
        response_data = {
            "count": self.page.paginator.count,
            "next": self.get_next_link(),
            "previous": self.get_previous_link(),
            "results": data,
        }
        mails = Mails.objects.all()
        custom_data = {
            "Total Mails": mails.count(),
            "Sent Mails": mails.filter(is_sent=True),
        }
        response_data.update(custom_data)

        return Response(data=response_data, status=HTTP_200_OK)


class ClientsPagination(PageNumberPagination):
    page_size = 5


class MessagesPagination(PageNumberPagination):
    page_size = 5
