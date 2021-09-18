from django.contrib.gis import admin

from .models import Location


class LocationAdmin(admin.OSMGeoAdmin):
    default_zoom = 5
    point_zoom = 20


admin.site.register(Location, LocationAdmin)
