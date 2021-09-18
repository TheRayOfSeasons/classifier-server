from core.services import Service

from core.database import ST_AsText


class LocationService(Service):
    """
    """

    table_name = 'locations'

    @property
    def coordinate_field(self):
        """
        Returns an SQL function call:

        ST_AsText("coordinates")
        """
        return ST_AsText(self.table.coordinates)


LOCATION_SERVICE = LocationService()