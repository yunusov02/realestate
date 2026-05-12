from django.http import HttpRequest
from django.shortcuts import render

from apps.home.service import PropertyService

from .types import (
    PropertyType, 
    PropertyStatus, 
    PropertyLocation,
)

# Create your views here.


def list_properties(request: HttpRequest):

    filters = {
        "type": request.GET.get("type"),
        "status": request.GET.get("status"),
        "location": request.GET.get("location"),
        "min_price": request.GET.get("min_price"),
        "max_price": request.GET.get("max_price"),
    }

    properties = PropertyService.get_filtered_properties(**filters)

    context = {
        "properties": properties,
        "filters": filters,
        "types": PropertyType.get_all_types(),
        "statuses": PropertyStatus.get_all_statuses(),
        "locations": PropertyLocation.get_all_locations(),
    }

    return render(request, "home/list_properties.html", context)


def property_detail(request: HttpRequest, property_id: int):

    property = PropertyService.get_property(property_id)
    
    return render(request, "home/property_detail.html", {"property": property})