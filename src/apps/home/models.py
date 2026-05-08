from django.db import models
from django.urls import reverse
from core.softdelete import SoftDelete, SoftDeleteManager
from .types import HomeCategory, Locality, HomeType


class Home(SoftDelete):
    title = models.CharField(max_length=255)

    type = models.CharField(max_length=50, choices=HomeType.choices)
    category = models.CharField(max_length=100, choices=HomeCategory.choices)

    price = models.DecimalField(max_digits=12, decimal_places=2)
    beds = models.PositiveIntegerField(blank=True, null=True)

    baths = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    property_sqft = models.PositiveIntegerField(blank=True, null=True)

    address = models.CharField(max_length=255)
    state = models.CharField(max_length=100, blank=True, null=True)
    main_address = models.CharField(max_length=255, blank=True, null=True)

    administrative_area_level_2 = models.CharField(
        max_length=255, blank=True, null=True
    )
    locality = models.CharField(max_length=20, choices=Locality.choices)
    sublocality = models.CharField(max_length=255, blank=True, null=True)

    street_name = models.CharField(max_length=255, blank=True, null=True)
    long_name = models.CharField(max_length=255, blank=True, null=True)
    formatted_address = models.CharField(max_length=512, blank=True, null=True)
    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, blank=True, null=True
    )
    longitude = models.DecimalField(
        max_digits=9, decimal_places=6, blank=True, null=True
    )

    def __str__(self):
        return self.title

    class Meta:
        db_table = "home"
        ordering = ["-created_at"]


class HomeImage(SoftDelete):
    home = models.ForeignKey(Home, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="home_images/")

    def __str__(self):
        return f"Image for {self.home.title}"
    
    
    class Meta:
        db_table = "home_image"
        ordering = ["-created_at"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})

