from django.db import models

# Create your models here.


class HomeCategory(models.TextChoices):
    CO_OP = "co-op", 'Co-op for sale'
    HOUSE_FOR_SALE = 'house-for-sale', 'House for sale'
    HOUSE_FOR_RENT = 'house-for-rent', 'House for rent'
    CONDO_FOR_SALE = 'condo-for-sale', 'Condo for sale'
    CONDO_FOR_RENT = 'condo-for-rent', 'Condo for rent'
    MULTI_FAMILY_FOR_SALE = 'multi-family-for-sale', 'Multi-family for sale'
    MULTI_FAMILY_FOR_RENT = 'multi-family-for-rent', 'Multi-family for rent'
    TOWNHOUSE_FOR_SALE = 'townhouse-for-sale', 'Townhouse for sale'
    TOWNHOUSE_FOR_RENT = 'townhouse-for-rent', 'Townhouse for rent'
    PENDING = 'pending', 'Pending'
    CONTINGENT = 'contingent', 'Contingent'
    LAND = 'land-for-sale', 'Land for sale'
    FOR_SALE = 'for-sale', 'For sale'
    FOR_RENT = 'for-rent', 'For rent'
    FORECLOSURE = 'foreclosure', 'Foreclosure'
    CONDOPLEX_FOR_SALE = 'condoplex-for-sale', 'Condoplex for sale'
    CONDOPLEX_FOR_RENT = 'condoplex-for-rent', 'Condoplex for rent'
    COMING_SOON = 'coming-soon', 'Coming soon'
    MOBILE_HOME_FOR_SALE = 'mobile-home-for-sale', 'Mobile home for sale'
    MOBILE_HOME_FOR_RENT = 'mobile-home-for-rent', 'Mobile home for rent'


class Locality(models.TextChoices):
    NEW_YORK = 'new-york', 'New York'
    LOS_ANGELES = 'los-angeles', 'Los Angeles'
    CHICAGO = 'chicago', 'Chicago'
    HOUSTON = 'houston', 'Houston'
    PHOENIX = 'phoenix', 'Phoenix'
    PHILADELPHIA = 'philadelphia', 'Philadelphia'
    SAN_ANTONIO = 'san-antonio', 'San Antonio'
    SAN_DIEGO = 'san-diego', 'San Diego'
    DALLAS = 'dallas', 'Dallas'
    SAN_JOSE = 'san-jose', 'San Jose'

class HomeType(models.TextChoices):
    APARTMENT = 'apartment', 'Apartment'
    HOUSE = 'house', 'House'
    VILLA = 'villa', 'Villa'
    CONDO = 'condo', 'Condo'


class Home(models.Model):
    title = models.CharField(max_length=255)
    broker_title = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=50, choices=HomeType.choices)
    category = models.CharField(max_length=100, choices=HomeCategory.choices)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    beds = models.PositiveIntegerField(blank=True, null=True)
    baths = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    property_sqft = models.PositiveIntegerField(blank=True, null=True)
    address = models.CharField(max_length=255)
    state = models.CharField(max_length=100, blank=True, null=True)
    main_address = models.CharField(max_length=255, blank=True, null=True)
    administrative_area_level_2 = models.CharField(max_length=255, blank=True, null=True)
    locality = models.CharField(max_length=20, choices=Locality.choices)
    sublocality = models.CharField(max_length=255, blank=True, null=True)
    street_name = models.CharField(max_length=255, blank=True, null=True)
    long_name = models.CharField(max_length=255, blank=True, null=True)
    formatted_address = models.CharField(max_length=512, blank=True, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)

    def __str__(self):
        return self.title
    


class HomeImage(models.Model):
    home = models.ForeignKey(Home, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='home_images/')

    def __str__(self):
        return f"Image for {self.home.title}"


