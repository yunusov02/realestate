from django.db import models


class PropertyType(models.TextChoices):
    daily_rental = "daily_rental", "Daily Rental"
    apartments = "apartments", "Apartments"
    commercial_properties = "commercial_properties", "Commercial Properties"
    houses = "houses", "Houses"
    lands = "lands", "Lands"
    
    
    @classmethod
    def get_all_types(cls):
        return [choice.value for choice in PropertyType]


class PropertyStatus(models.TextChoices):
    for_sale = "for_sale", "For Sale"
    for_rent = "for_rent", "For Rent"
    sold = "sold", "Sold"
    rented = "rented", "Rented"
    
    @classmethod
    def get_all_statuses(cls):
        return [choice.value for choice in PropertyStatus]


class PropertyLocation(models.TextChoices):
    city_center = "city_center", "City Center"
    suburbs = "suburbs", "Suburbs"
    countryside = "countryside", "Countryside"
    outside_city = "outside_city", "Outside City"
    
    @classmethod
    def get_all_locations(cls):
        return [choice.value for choice in PropertyLocation]


class HouseBathroomType(models.TextChoices):
    combined = "combined", "Combined"
    separate = "separate", "Separate"
    


class HouseFurnishingType(models.TextChoices):
    furnished = "furnished", "Furnished"
    unfurnished = "unfurnished", "Unfurnished"
    semi_furnished = "semi_furnished", "Semi-Furnished"


class HouseHeatingType(models.TextChoices):
    central_heating = "central_heating", "Central Heating"
    individual_heating = "individual_heating", "Individual Heating"
    no_heating = "no_heating", "No Heating"


class HouseCoolingType(models.TextChoices):
    central_cooling = "central_cooling", "Central Cooling"
    individual_cooling = "individual_cooling", "Individual Cooling"
    no_cooling = "no_cooling", "No Cooling"


class HouseParkingType(models.TextChoices):
    garage = "garage", "Garage"
    driveway = "driveway", "Driveway"
    street_parking = "street_parking", "Street Parking"
    no_parking = "no_parking", "No Parking"


class BuildingMaterialType(models.TextChoices):
    brick = "brick", "Brick"
    concrete = "concrete", "Concrete"
    wood = "wood", "Wood"
    steel = "steel", "Steel"
    other = "other", "Other"


class HouseRenovationType(models.TextChoices):
    renovated = "renovated", "Renovated"
    needs_renovation = "needs_renovation", "Needs Renovation"
    recently_renovated = "recently_renovated", "Recently Renovated"
    no_renovation_needed = "no_renovation_needed", "No Renovation Needed"
