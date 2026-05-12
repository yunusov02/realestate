from django.db import models
from core.softdelete import SoftDelete
from . import types
from apps.helper.models import Utility, Nearby


class Property(SoftDelete):

    title = models.CharField(max_length=255)
    description = models.TextField()

    type = models.CharField(max_length=40, choices=types.PropertyType.choices)
    status = models.CharField(max_length=40, choices=types.PropertyStatus.choices)
    location = models.CharField(max_length=40, choices=types.PropertyLocation.choices)

    price = models.DecimalField(max_digits=10, decimal_places=2)
    area = models.DecimalField(max_digits=10, decimal_places=2)

    longitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True
    )
    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Properties"
        db_table = "properties"
        ordering = ["title"]


class PropertyUtility(models.Model):
    property = models.ForeignKey(
        Property, related_name="utilities", on_delete=models.CASCADE
    )
    utility = models.ForeignKey(
        Utility, related_name="property_utilities", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.utility.name} for {self.property.title}"

    class Meta:
        verbose_name_plural = "Property Utilities"
        db_table = "property_utilities"


class PropertyNearby(models.Model):
    property = models.ForeignKey(
        Property, related_name="nearby", on_delete=models.CASCADE
    )
    nearby = models.ForeignKey(
        Nearby, related_name="property_nearby", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.nearby.name} near {self.property.title}"

    class Meta:
        verbose_name_plural = "Property Nearby"
        db_table = "property_nearby"


class PropertyImage(SoftDelete):
    property = models.ForeignKey(
        Property, related_name="images", on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="property_images/")

    def __str__(self):
        return f"Image for {self.property.title}"

    class Meta:
        verbose_name_plural = "Property Images"
        db_table = "property_images"


class Lands(SoftDelete):

    property = models.OneToOneField(
        Property, related_name="land_details", on_delete=models.CASCADE
    )
    agrocultural_land = models.BooleanField(default=False)
    residential_land = models.BooleanField(default=False)
    commercial_land = models.BooleanField(default=False)
    road_access = models.BooleanField(default=False)
    water_access = models.BooleanField(default=False)

    def __str__(self):
        return f"Land details for {self.property.title}"

    class Meta:
        verbose_name_plural = "Lands"
        db_table = "lands"


class Houses(SoftDelete):

    property = models.OneToOneField(
        Property, related_name="house_details", on_delete=models.CASCADE
    )
    bedrooms = models.IntegerField()
    floor = models.IntegerField()
    number_of_floors = models.IntegerField()
    bathrooms = models.IntegerField()
    bathroom_type = models.CharField(
        max_length=40, choices=types.HouseBathroomType.choices
    )
    furnishing_type = models.CharField(
        max_length=40, choices=types.HouseFurnishingType.choices
    )
    heating_type = models.CharField(
        max_length=40, choices=types.HouseHeatingType.choices
    )
    cooling_type = models.CharField(
        max_length=40, choices=types.HouseCoolingType.choices
    )
    parking_type = models.CharField(
        max_length=40, choices=types.HouseParkingType.choices
    )
    building_material_type = models.CharField(
        max_length=40, choices=types.BuildingMaterialType.choices
    )
    renovation_type = models.CharField(
        max_length=40, choices=types.HouseRenovationType.choices
    )

    def __str__(self):
        return f"House details for {self.property.title}"

    class Meta:
        verbose_name_plural = "Houses"
        db_table = "houses"
