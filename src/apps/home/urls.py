
from django.urls import path

from apps.home.views import list_properties, property_detail

app_name = "apps.home"

urlpatterns = [
    path("properties/", list_properties, name="list_properties"),
    path("properties/<int:property_id>/", property_detail, name="property_detail"),
]

