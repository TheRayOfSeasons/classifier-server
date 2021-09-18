from django.db import models

from core.models import BaseModel
from locations.models import Location
from trees.models import Tree


class StateOfDecay:
    """
    """

    LOOSE = 'loose'
    MODERATELY_INTACT = 'moderately_intact'
    INTACT = 'intact'

    CHOICES = (
        (LOOSE, 'Loose'),
        (MODERATELY_INTACT, 'Moderately Intact'),
        (INTACT, 'Intact')
    )


class BarkTexture:
    """
    """

    SMOOTH = 'smooth'
    ROUGH = 'rough'

    CHOICES = (
        (SMOOTH, 'Smooth'),
        (ROUGH, 'Rough')
    )


class EpiphyticOrganism(BaseModel):
    """
    """

    name = models.CharField(max_length=64)

    class Meta:
        db_table = 'epiphytic_organisms'


class SpecimenDirectionalBreakdown(models.Model):
    """
    """

    first = models.DecimalField(max_digits=16, decimal_places=8)
    second = models.DecimalField(max_digits=16, decimal_places=8)
    third = models.DecimalField(max_digits=16, decimal_places=8)

    class Meta:
        db_table = 'specimen_directional_breakdowns'


class SpecimenDirectionData(models.Model):
    """
    """

    north = models.ForeignKey(
        SpecimenDirectionalBreakdown,
        on_delete=models.CASCADE,
        related_name='specimens_north_direction_set'
    )
    west = models.ForeignKey(
        SpecimenDirectionalBreakdown,
        on_delete=models.CASCADE,
        related_name='specimens_west_direction_set'
    )
    east = models.ForeignKey(
        SpecimenDirectionalBreakdown,
        on_delete=models.CASCADE,
        related_name='specimens_east_direction_set'
    )
    south = models.ForeignKey(
        SpecimenDirectionalBreakdown,
        on_delete=models.CASCADE,
        related_name='specimens_south_direction_set'
    )

    class Meta:
        db_table = 'specimen_direction_data'


class Specimen(BaseModel):
    """
    """

    name = models.CharField(max_length=64, blank=True)
    host_tree = models.ForeignKey(Tree, on_delete=models.PROTECT)
    location = models.ForeignKey(Location, on_delete=models.PROTECT)
    with_stain = models.BooleanField(default=False)
    state_of_decay = models.CharField(
        max_length=32, choices=StateOfDecay.CHOICES)
    bark_texture = models.CharField(max_length=8, choices=BarkTexture.CHOICES)
    direction_data = models.ForeignKey(
        SpecimenDirectionData, on_delete=models.CASCADE)
    date_of_collection = models.DateTimeField()

    class Meta:
        db_table = 'specimens'


class SpecimenEpiphyticOrganism(models.Model):
    """
    Many to Many table for specimens and epiphytes.
    """

    specimen = models.ForeignKey(Specimen, on_delete=models.CASCADE)
    epiphytic_organism = models.ForeignKey(
        EpiphyticOrganism, on_delete=models.CASCADE)

    class Meta:
        db_table = 'specimen_epiphytic_organisms'
