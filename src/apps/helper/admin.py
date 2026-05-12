from django.contrib import admin

from .models import Utility, Nearby


@admin.register(Utility)
class UtilityAdmin(admin.ModelAdmin):
    list_display = ("name", "count")
    search_fields = ("name",)

@admin.register(Nearby)
class NearbyAdmin(admin.ModelAdmin):
    list_display = ("name", "count")
    search_fields = ("name",)
    
    
