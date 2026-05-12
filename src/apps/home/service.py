from apps.helper.models import Utility, Nearby

from .models import ( 
    Property, 
    PropertyUtility, 
    PropertyNearby, 
    PropertyImage,
    PropertyUtility,
    PropertyNearby,
    Lands,
    Houses
)

from .types import (
    PropertyType, 
    PropertyStatus, 
    PropertyLocation, 
    
    HouseBathroomType, 
    HouseFurnishingType, 
    HouseHeatingType, 
    HouseCoolingType, 
    HouseParkingType
)

class PropertyService:
    def __init__(self, test):
        self.test = None

    @classmethod
    def get_all_properties(cls):
        return Property.objects.all()

    @classmethod
    def get_filtered_properties(cls, type=None, status=None, location=None, min_price=None, max_price=None):
        qs = Property.objects.all()
        if type:
            qs = qs.filter(type=type)
        if status:
            qs = qs.filter(status=status)
        if location:
            qs = qs.filter(location=location)
        if min_price:
            qs = qs.filter(price__gte=min_price)
        if max_price:
            qs = qs.filter(price__lte=max_price)
        return qs
    
    @classmethod
    def get_property(cls, property_id):
        return Property.objects.get(id=property_id)
    
    @classmethod
    def create_property(cls, data):
        property = Property.objects.create(**data)
        return property
    
    @classmethod
    def update_property(cls, property_id, data):
        property = Property.objects.get(id=property_id)
        for key, value in data.items():
            setattr(property, key, value)
        property.save()
        return property
    
    @classmethod
    def delete_property(cls, property_id):
        property = Property.objects.get(id=property_id)
        property.delete()
        return property


class PropertyUtilityService:
    
    @classmethod
    def get_all_property_utilities(cls, property_id):
        return PropertyUtility.objects.filter(property_id=property_id)

    @classmethod
    def create_property_utility(cls, property_id, utility_id):
        property = Property.objects.get(id=property_id)
        utility = Utility.objects.get(id=utility_id)
        property_utility = PropertyUtility.objects.create(property=property, utility=utility)
        return property_utility
    
    
class PropertyNearbyService:
    @classmethod
    def get_all_property_nearbies(cls, property_id):
        return PropertyNearby.objects.filter(property_id=property_id)

    @classmethod
    def create_property_nearby(cls, property_id, nearby_id):
        property = Property.objects.get(id=property_id)
        nearby = Nearby.objects.get(id=nearby_id)
        property_nearby = PropertyNearby.objects.create(property=property, nearby=nearby)
        return property_nearby