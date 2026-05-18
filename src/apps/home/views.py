from django.http import HttpRequest
from django.shortcuts import render, redirect

from apps.home.service import PropertyService
from apps.home.forms import PropertyForm

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
    
    for image in property.images.all():
        print(image.image.url)
        
    return render(request, "home/property_detail.html", {"property": property})



def create_property(request: HttpRequest):

    form = PropertyForm()
    
    if request.method == "POST":
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            property = form.save()
            return redirect("apps.home:property_detail", property_id=property.id)
        
    
    context = {
        "form": form,
    }
    return render(request, "home/create_property.html", context)



def delete_property(request: HttpRequest, property_id: int):
    
    if request.method != "POST":
        return redirect("apps.home:property_detail", property_id=property_id)
    else:
        PropertyService.delete_property(property_id)
        return redirect("apps.home:list_properties")
    
