
from django.urls import path

from apps.home.views import list_properties, property_detail, create_property

app_name = "apps.home"

urlpatterns = [
    path("properties/", list_properties, name="list_properties"),
    path("properties/<int:property_id>/", property_detail, name="property_detail"),
    path("properties/create/", create_property, name="create_property"),
]

