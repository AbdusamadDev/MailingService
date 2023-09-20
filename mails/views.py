from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from mails import pagination, filters, serializers, models


class MailingViewset(ModelViewSet):
    pagination_class = pagination.MailingPagination
    filterset_class = [filters.MailingFilterSet]
    serializer_class = serializers.MailingSerializer
    queryset = models.Mails.objects.all()
    model = models.Mails

    @action(detail=False, methods=["get"])
    def statistics(self, request, *args, **kwargs):
        self.pagination_class = (
            pagination.MailingStatisticsPagination
        )  # Set the custom pagination for this action
        response = self.pagination_class().get_paginated_response(data=request)
        return response


class ClientsViewSet(ModelViewSet):
    model = models.Client
    serializer_class = serializers.ClientsSerializer
    pagination_class = pagination.ClientsPagination
    queryset = models.Client.objects.all()


class MessagesViewSet(ModelViewSet):
    model = models.Message
    serializer_class = serializers.MessagesSerializer
    pagination_class = pagination.MessagesPagination
    queryset = models.Message.objects.all()

    def list(self, request, *args, **kwargs):
        paginated_queryset = self.paginate_queryset(self.queryset)
        print(paginated_queryset)
        context = serializers.MessagesStatisticsSerializer(
            paginated_queryset, many=True
        )
        return self.get_paginated_response(context.data)
