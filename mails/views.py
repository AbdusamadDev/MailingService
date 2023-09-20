from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

from mails import (
    pagination,
    filters,
    serializers,
    models,
)


class MailingViewSet(ModelViewSet):
    """
    Base CRUD for Mailings. All stay default but adding statistics functionality.
    """

    pagination_class = pagination.MailingPagination
    filterset_class = [filters.MailingFilterSet]
    serializer_class = serializers.MailingSerializer
    queryset = models.Mails.objects.all()
    model = models.Mails

    # Special listing (fetching statistics) as required in the task
    @action(detail=False, methods=["get"])
    def statistics(self, request, *args, **kwargs):
        self.pagination_class = (
            pagination.MailingStatisticsPagination
        )  # Set the custom pagination for this action
        response = self.pagination_class().get_paginated_response(
            request=request,
            queryset=self.queryset,
            serializer=serializers.MailingSerializer,
        )
        return response


class ClientsViewSet(ModelViewSet):
    """
    Base CRUD for Clients. All methods stay default, no need to customize
    because of task requirements.
    """

    model = models.Client
    serializer_class = serializers.ClientsSerializer
    pagination_class = pagination.ClientsPagination
    queryset = models.Client.objects.all()


class MessagesViewSet(ModelViewSet):
    """
    Base CRUD for messages. Delete, Update, Details option stays default.
    """

    model = models.Message
    serializer_class = serializers.MessagesSerializer
    pagination_class = pagination.MessagesPagination
    queryset = models.Message.objects.all()

    # Special listing (fetching statistics) as required in the task
    @action(detail=False, methods=["get"])
    def statistics(self, request):
        """
        Another option for fetching statistics from database is looping QuerSet from database
        and attach them each other and adding custom context into serializers.
        But the issue is looping out millions of data from database hurts database and
        performance, for that reason, operations like attaching and building a
        statistics were done by the combination of django pagination, serializers and views
        (without looping).
        """
        self.pagination_class = pagination.MessagesStatisticsPagination
        response = self.pagination_class().get_paginated_response(
            request=request,
            queryset=self.queryset,
            serializer=serializers.MessagesStatisticsSerializer,
        )
        return response

    # Standard Listing of rows from database
    def list(self, request, *args, **kwargs):
        paginated_queryset = self.paginate_queryset(self.queryset)
        print(paginated_queryset)
        context = serializers.MessagesStatisticsSerializer(
            paginated_queryset, many=True
        )
        return self.get_paginated_response(context.data)
