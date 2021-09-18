from django.contrib import admin

from .models import EpiphyticOrganism
from .models import Specimen
from .models import SpecimenDirectionalBreakdown
from .models import SpecimenDirectionData
from .models import SpecimenEpiphyticOrganism


admin.site.register(EpiphyticOrganism)
admin.site.register(Specimen)
admin.site.register(SpecimenDirectionalBreakdown)
admin.site.register(SpecimenDirectionData)
admin.site.register(SpecimenEpiphyticOrganism)
