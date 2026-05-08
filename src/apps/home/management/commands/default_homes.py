from django.core.management.base import BaseCommand
from faker import Faker
from apps.home.models import Home, HomeImage
from apps.home.service import HomeService



def create_default_homes():
    
    faker = Faker()
    
    
    
    
    for _ in range(50):
        home = Home(
            title=faker.sentence(nb_words=4),
            type=faker.random_element(elements=["Apartment", "House", "Condo"]),
            category=faker.random_element(elements=["For Sale", "For Rent"]),
            price=round(faker.random_number(digits=6) / 100, 2),
            beds=faker.random_int(min=1, max=5),
            baths=round(faker.random_number(digits=2) / 10, 1),
            property_sqft=faker.random_int(min=500, max=5000),
            address=faker.street_address(),
            state=faker.state(),
            locality=faker.random_element(elements=["Urban", "Suburban", "Rural"]),
        )
        HomeService.create_home(home)
        
        
    
