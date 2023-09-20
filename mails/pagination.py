from rest_framework.pagination import PageNumberPagination
from rest_framework.status import HTTP_200_OK
from rest_framework.response import Response

from mails.models import Mails, Message, Client
from mails.serializers import MailingSerializer


class MailingPagination(PageNumberPagination):
    page_size = 5


class MailingStatisticsPagination(PageNumberPagination):
    page_size = 5

    def paginate_sent_mails(self, queryset, request, page_param):
        # Use self for pagination setup
        self.page_query_param = page_param
        page = self.paginate_queryset(queryset, request)
        if page is not None:
            return (
                self.page.paginator.count,
                self.get_next_link(),
                self.get_previous_link(),
                page,
            )
        return None

    def get_paginated_response(self, data):
        mails = Mails.objects.all()

        (
            sent_mails_count,
            sent_next_link,
            sent_previous_link,
            sent_mails_page,
        ) = self.paginate_sent_mails(mails.filter(status="Sent"), data, "sent_mails")
        (
            pending_mails_count,
            pending_next_link,
            pending_previous_link,
            pending_mails_page,
        ) = self.paginate_sent_mails(
            mails.filter(status="Not Sent"), data, "pending_mails"
        )

        sent_mails_serializer = MailingSerializer(instance=sent_mails_page, many=True)
        pending_mails_serializer = MailingSerializer(
            instance=pending_mails_page, many=True
        )

        response_data = {
            "Total Mails": mails.count(),
            "Sent Mails": {
                "count": sent_mails_count,
                "next": sent_next_link,
                "previous": sent_previous_link,
                "results": sent_mails_serializer.data,
            },
            "Pending Mails": {
                "count": pending_mails_count,
                "next": pending_next_link,
                "previous": pending_previous_link,
                "results": pending_mails_serializer.data,
            },
        }

        return Response(data=response_data, status=HTTP_200_OK)


class ClientsPagination(PageNumberPagination):
    page_size = 5


class MessagesPagination(PageNumberPagination):
    page_size = 5
