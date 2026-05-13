from decimal import Decimal

from django.test import TestCase
from django.urls import reverse

from apps.home.models import Property
from apps.home.service import PropertyService
from apps.home.types import PropertyType, PropertyStatus, PropertyLocation


class HomeTests(TestCase):
    def setUp(self):
        self.property_1 = Property.objects.create(
            title="Cozy City House",
            description="A lovely house in the city center.",
            type=PropertyType.houses,
            status=PropertyStatus.for_sale,
            location=PropertyLocation.city_center,
            price=Decimal("1200.00"),
            area=Decimal("95.00"),
        )
        self.property_2 = Property.objects.create(
            title="Suburban Apartment",
            description="A modern apartment in the suburbs.",
            type=PropertyType.apartments,
            status=PropertyStatus.for_rent,
            location=PropertyLocation.suburbs,
            price=Decimal("850.00"),
            area=Decimal("72.00"),
        )
        self.property_3 = Property.objects.create(
            title="Country Land Plot",
            description="Spacious land outside the city.",
            type=PropertyType.lands,
            status=PropertyStatus.for_sale,
            location=PropertyLocation.countryside,
            price=Decimal("450.00"),
            area=Decimal("1200.00"),
        )

    def test_list_properties_view_returns_all_properties(self):
        url = reverse("apps.home:list_properties")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home/list_properties.html")
        self.assertEqual(response.context["properties"].count(), 3)
        self.assertContains(response, self.property_1.title)
        self.assertContains(response, self.property_2.title)
        self.assertContains(response, self.property_3.title)
        self.assertEqual(response.context["filters"], {
            "type": None,
            "status": None,
            "location": None,
            "min_price": None,
            "max_price": None,
        })
        self.assertListEqual(
            response.context["types"], PropertyType.get_all_types()
        )
        self.assertListEqual(
            response.context["statuses"], PropertyStatus.get_all_statuses()
        )
        self.assertListEqual(
            response.context["locations"], PropertyLocation.get_all_locations()
        )

    def test_list_properties_view_applies_filters(self):
        url = reverse("apps.home:list_properties")
        response = self.client.get(
            url,
            {
                "type": PropertyType.houses,
                "status": PropertyStatus.for_sale,
                "location": PropertyLocation.city_center,
                "min_price": "1000",
                "max_price": "1300",
            },
        )

        self.assertEqual(response.status_code, 200)
        properties = list(response.context["properties"])
        self.assertEqual(len(properties), 1)
        self.assertEqual(properties[0], self.property_1)
        self.assertContains(response, self.property_1.title)
        self.assertNotContains(response, self.property_2.title)
        self.assertNotContains(response, self.property_3.title)

    def test_property_detail_view_displays_property(self):
        url = reverse(
            "apps.home:property_detail",
            kwargs={"property_id": self.property_2.id},
        )
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home/property_detail.html")
        self.assertEqual(response.context["property"], self.property_2)
        self.assertContains(response, self.property_2.title)
        self.assertContains(response, self.property_2.description)

    def test_property_service_get_filtered_properties(self):
        filtered = PropertyService.get_filtered_properties(
            type=PropertyType.apartments,
            status=PropertyStatus.for_rent,
            location=PropertyLocation.suburbs,
            min_price=Decimal("800.00"),
            max_price=Decimal("900.00"),
        )

        self.assertQuerysetEqual(
            filtered.order_by("id"),
            [repr(self.property_2)],
            ordered=True,
        )

    def test_property_service_get_property_raises_when_missing(self):
        invalid_id = self.property_3.id + 999
        with self.assertRaises(Property.DoesNotExist):
            PropertyService.get_property(invalid_id)
