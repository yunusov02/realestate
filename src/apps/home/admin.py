from django.contrib import admin

from .models import (
    Property,
    PropertyImage,
    PropertyUtility,
    PropertyNearby,
    Lands,
    Houses
)


class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 1


class PropertyUtilityInline(admin.TabularInline):
    model = PropertyUtility
    extra = 1


class PropertyNearbyInline(admin.TabularInline):
    model = PropertyNearby
    extra = 1


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ("title", "type", "status", "location", "price")
    search_fields = ("title", "description")
    list_filter = ("type", "status", "location")
    inlines = (PropertyImageInline, PropertyUtilityInline, PropertyNearbyInline)


admin.site.register(Lands)
admin.site.register(Houses)