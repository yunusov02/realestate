from django.db import models


class HomeCategory(models.TextChoices):
    CO_OP = "co-op", "Co-op for sale"
    HOUSE_FOR_SALE = "house-for-sale", "House for sale"
    HOUSE_FOR_RENT = "house-for-rent", "House for rent"
    CONDO_FOR_SALE = "condo-for-sale", "Condo for sale"
    CONDO_FOR_RENT = "condo-for-rent", "Condo for rent"
    MULTI_FAMILY_FOR_SALE = "multi-family-for-sale", "Multi-family for sale"
    MULTI_FAMILY_FOR_RENT = "multi-family-for-rent", "Multi-family for rent"
    TOWNHOUSE_FOR_SALE = "townhouse-for-sale", "Townhouse for sale"
    TOWNHOUSE_FOR_RENT = "townhouse-for-rent", "Townhouse for rent"
    PENDING = "pending", "Pending"
    CONTINGENT = "contingent", "Contingent"
    LAND = "land-for-sale", "Land for sale"
    FOR_SALE = "for-sale", "For sale"
    FOR_RENT = "for-rent", "For rent"
    FORECLOSURE = "foreclosure", "Foreclosure"
    CONDOPLEX_FOR_SALE = "condoplex-for-sale", "Condoplex for sale"
    CONDOPLEX_FOR_RENT = "condoplex-for-rent", "Condoplex for rent"
    COMING_SOON = "coming-soon", "Coming soon"
    MOBILE_HOME_FOR_SALE = "mobile-home-for-sale", "Mobile home for sale"
    MOBILE_HOME_FOR_RENT = "mobile-home-for-rent", "Mobile home for rent"


class Locality(models.TextChoices):
    NEW_YORK = "new-york", "New York"
    LOS_ANGELES = "los-angeles", "Los Angeles"
    CHICAGO = "chicago", "Chicago"
    HOUSTON = "houston", "Houston"
    PHOENIX = "phoenix", "Phoenix"
    PHILADELPHIA = "philadelphia", "Philadelphia"
    SAN_ANTONIO = "san-antonio", "San Antonio"
    SAN_DIEGO = "san-diego", "San Diego"
    DALLAS = "dallas", "Dallas"
    SAN_JOSE = "san-jose", "San Jose"


class HomeType(models.TextChoices):
    APARTMENT = "apartment", "Apartment"
    HOUSE = "house", "House"
    VILLA = "villa", "Villa"
    CONDO = "condo", "Condo"
