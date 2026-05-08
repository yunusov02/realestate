from enum import Enum
from django.db import models



class HomeCategory(str, Enum):
    CO_OP = "co-op"
    HOUSE_FOR_SALE = "house-for-sale"
    HOUSE_FOR_RENT = "house-for-rent"
    CONDO_FOR_SALE = "condo-for-sale"
    CONDO_FOR_RENT = "condo-for-rent"
    MULTI_FAMILY_FOR_SALE = "multi-family-for-sale"
    MULTI_FAMILY_FOR_RENT = "multi-family-for-rent"
    TOWNHOUSE_FOR_SALE = "townhouse-for-sale"
    TOWNHOUSE_FOR_RENT = "townhouse-for-rent"
    PENDING = "pending"
    CONTINGENT = "contingent"
    LAND = "land-for-sale"
    FOR_SALE = "for-sale"
    FOR_RENT = "for-rent"
    FORECLOSURE = "foreclosure"
    CONDOPLEX_FOR_SALE = "condoplex-for-sale"
    CONDOPLEX_FOR_RENT = "condoplex-for-rent"
    COMING_SOON = "coming-soon"
    MOBILE_HOME_FOR_SALE = "mobile-home-for-sale"
    MOBILE_HOME_FOR_RENT = "mobile-home-for-rent"

    
    @classmethod
    def get_list_of_categories(cls):
        return [category.value for category in HomeCategory]


class Locality(str, Enum):
    NEW_YORK = "new-york"
    LOS_ANGELES = "los-angeles"
    CHICAGO = "chicago"
    HOUSTON = "houston"
    PHOENIX = "phoenix"
    PHILADELPHIA = "philadelphia"
    SAN_ANTONIO = "san-antonio"
    SAN_DIEGO = "san-diego"
    DALLAS = "dallas"
    SAN_JOSE = "san-jose"

    
    @classmethod
    def get_list_of_localities(cls):
        return [locality.value for locality in Locality]


class HomeType(str, Enum):
    APARTMENT = "apartment"
    HOUSE = "house"
    VILLA = "villa"
    CONDO = "condo"


    @classmethod
    def get_list_of_types(cls):
        return [home_type.value for home_type in HomeType]

