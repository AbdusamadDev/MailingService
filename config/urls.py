from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.routers import DefaultRouter

from mails.views import (
    MailingViewSet,
    MessagesViewSet,
    ClientsViewSet,
)

router = DefaultRouter()
router.register(r"mails", MailingViewSet)
router.register(r"messages", MessagesViewSet)
router.register(r"clients", ClientsViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Notification Service for testing",
        default_version="v1",
        description="This is a public openapi info",
        terms_of_service="https://www.termsfeed.com/live/6ae1964f-78a1-4c1f-9c79-0ee628a42128",  # Just a public terms of service link
        contact=openapi.Contact(email="abdusamaddev571@gmail.com"),
        license=openapi.License(name="Notification Service Public Licence"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path(
        "docs/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
