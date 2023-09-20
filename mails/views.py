from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

from mails import (
    pagination,
    filters,
    serializers,
    models,
)


class MailingViewSet(ModelViewSet):
    pagination_class = pagination.MailingPagination
    filterset_class = [filters.MailingFilterSet]
    serializer_class = serializers.MailingSerializer
    queryset = models.Mails.objects.all()
    model = models.Mails

    # Full statistics for Mailings
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
    model = models.Client
    serializer_class = serializers.ClientsSerializer
    pagination_class = pagination.ClientsPagination
    queryset = models.Client.objects.all()


class MessagesViewSet(ModelViewSet):
    model = models.Message
    serializer_class = serializers.MessagesSerializer
    pagination_class = pagination.MessagesPagination
    queryset = models.Message.objects.all()

    @action(detail=False, methods=["get"])
    def statistics(self, request):
        self.pagination_class = pagination.MessagesStatisticsPagination
        response = self.pagination_class().get_paginated_response(
            request=request,
            queryset=self.queryset,
            serializer=serializers.MessagesStatisticsSerializer,
        )
        return response

    def list(self, request, *args, **kwargs):
        paginated_queryset = self.paginate_queryset(self.queryset)
        print(paginated_queryset)
        context = serializers.MessagesStatisticsSerializer(
            paginated_queryset, many=True
        )
        return self.get_paginated_response(context.data)


# {
#     "Total messages": 51,
#     "Sent Messages": {
#         "Count": 25,
#         "next_page": "http://127.0.0.2",
#         "results": [
#             {"asfasf": "asdfasdf", "asdfasdf": "sadfsafasasfasf", "asdf": 786453124},
#             {"asfasf": "asdfasdf", "asdfasdf": "sadfsafasasfasf", "asdf": 786453124},
#         ],
#     },
#     "Pending Messages": {
#         "next_page": "http://127.0.0.2",
#         "results": [
#             {"asfasf": "asdfasdf", "asdfasdf": "sadfsafasasfasf", "asdf": 786453124},
#             {"asfasf": "asdfasdf", "asdfasdf": "sadfsafasasfasf", "asdf": 786453124},
#         ],
#     },
# }
