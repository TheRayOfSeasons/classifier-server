from django.contrib.gis.db import models

from core.models import BaseModel


class Location(BaseModel):
    """
    A recorded location.
    """

    name = models.CharField(max_length=128)
    coordinates = models.PointField(blank=True, null=True)
    altitude = models.DecimalField(max_digits=16, decimal_places=8)

    class Meta:
        db_table = 'locations'
