from django.core.management.base import BaseCommand
from faker import Faker
from apps.home.service import PropertyService, PropertyUtilityService, PropertyNearbyService

from apps.home.types import (
    PropertyType, 
    PropertyStatus, 
    PropertyLocation,
    HouseBathroomType, 
    HouseFurnishingType,
    HouseHeatingType,
    HouseCoolingType,
    HouseParkingType
)

from apps.helper.service import UtilityService, NearbyService
from apps.helper.models import Utility, Nearby


class Command(BaseCommand):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.faker = Faker()
        
        
    def handle(self, *args, **options):
        
        nearbies = list(NearbyService.get_all_nearbies())
        utilities = list(UtilityService.get_all_utilities())

        for _ in range(10):
            data = {
                "title": self.faker.sentence(),
                "description": self.faker.text(),
                "type": self.faker.random_element(elements=[choice[0] for choice in PropertyType.choices]),
                "status": self.faker.random_element(elements=[choice[0] for choice in PropertyStatus.choices]),
                "location": self.faker.random_element(elements=[choice[0] for choice in PropertyLocation.choices]),
                "price": self.faker.random_number(digits=5),
                "area": self.faker.random_number(digits=3),
                "longitude": self.faker.longitude(),
                "latitude": self.faker.latitude(),
            }
            property = PropertyService.create_property(data)

            selected_utilities = self.faker.random_elements(elements=utilities, length=3, unique=True)
            selected_nearbies = self.faker.random_elements(elements=nearbies, length=3, unique=True)
            
            for utility in selected_utilities:
                PropertyUtilityService.create_property_utility(property_id=property.id, utility_id=utility.id)

            for nearby in selected_nearbies:
                PropertyNearbyService.create_property_nearby(property_id=property.id, nearby_id=nearby.id)
                
        self.stdout.write(self.style.SUCCESS("Successfully created default properties"))