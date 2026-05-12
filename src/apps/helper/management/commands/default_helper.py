from django.core.management.base import BaseCommand
from apps.helper.models import Utility, Nearby


class Command(BaseCommand):
    help = "Create default utilities and nearby places"

    def handle(self, *args, **kwargs):
        utilities = [
            "Electricity",
            "Water",
            "Gas",
            "Internet",
            "Cable TV",
            "Trash Collection",
        ]
        nearby_places = [
            "School",
            "Hospital",
            "Supermarket",
            "Park",
            "Public Transport",
            "Gym",
        ]

        for utility in utilities:
            Utility.objects.get_or_create(name=utility)

        for place in nearby_places:
            Nearby.objects.get_or_create(name=place)

        self.stdout.write(
            self.style.SUCCESS(
                "Default utilities and nearby places created successfully."
            )
        )
