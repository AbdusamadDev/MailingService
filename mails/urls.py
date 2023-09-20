from rest_framework.urlpatterns import path

from mails.views import MailingViewset, ClientsViewSet, MessagesViewSet


urlpatterns = [
    path(
        "mails/",
        MailingViewset.as_view({"get": "list", "post": "create"}),
    ),
    path(
        "mails/<int:pk>/",
        MailingViewset.as_view({"put": "update", "get": "detail", "delete": "destroy"}),
    ),
    path(
        "clients/",
        ClientsViewSet.as_view({"get": "list", "post": "create"}),
    ),
    path(
        "messages/",
        MessagesViewSet.as_view({"get": "list", "post": "create"}),
    ),
]
