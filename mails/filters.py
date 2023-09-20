from django_filters import FilterSet

from mails.models import Mails


class MailingFilterSet(FilterSet):
    """
    FilterSet for filtering mails with client's mobile code and tag
    Was used external library called django-filter because of scalablity
    """

    class Meta:
        model = Mails
        fields = ["client_tag", "client_phone_code"]
