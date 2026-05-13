from django.contrib import admin
from django.urls import include, path

from .views import landing_page

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", landing_page, name="landing_page"),
    path("", include("apps.home.urls")),
    path("users/", include("apps.users.urls")),
]


