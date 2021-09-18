from django.db import models

from core.models import BaseModel
from core.models import ForeignFileModel
from core.models import OrderedModel
from trees.models import Tree


class Substrate(BaseModel):
    """
    """

    name = models.CharField(max_length=64)

    class Meta:
        db_table = 'substrates'


class FruitingBody(BaseModel):
    """
    """

    # 0/1
    is_passed = models.BooleanField(default=False)

    class Meta:
        db_table = 'fruiting_bodies'


class FruitingBodyImage(OrderedModel, ForeignFileModel, BaseModel):
    """
    Will contain the address of the image in the S3 bucket
    """

    fruiting_body = models.ForeignKey(FruitingBody, on_delete=models.PROTECT)

    class Meta:
        db_table = 'fruiting_body_images'


class FruitingBodyDirections(models.Model):
    """
    Directional data for plasmodiums.
    """

    north = models.ForeignKey(
        FruitingBody,
        on_delete=models.PROTECT,
        related_name='fruitingbody_north_direction_set',
        blank=True,
        null=True
    )
    west = models.ForeignKey(
        FruitingBody,
        on_delete=models.PROTECT,
        related_name='fruitingbody_west_direction_set',
        blank=True,
        null=True
    )
    east = models.ForeignKey(
        FruitingBody,
        on_delete=models.PROTECT,
        related_name='fruitingbody_east_direction_set',
        blank=True,
        null=True
    )
    south = models.ForeignKey(
        FruitingBody,
        on_delete=models.PROTECT,
        related_name='fruitingbody_south_direction_set',
        blank=True,
        null=True
    )

    class Meta:
        db_table = 'fruiting_body_directions'


class Plasmodium(BaseModel):
    """
    """

    # 0/1
    is_passed = models.BooleanField(default=False)

    class Meta:
        db_table = 'plasmodiums'


class PlasmodiumImage(OrderedModel, ForeignFileModel, BaseModel):
    """
    Will contain the address of the image in the S3 bucket
    """

    plasmodium = models.ForeignKey(Plasmodium, on_delete=models.PROTECT)

    class Meta:
        db_table = 'plasmodium_images'


class PlasmodiumDirections(models.Model):
    """
    Directional data for plasmodiums.
    """

    north = models.ForeignKey(
        Plasmodium,
        on_delete=models.PROTECT,
        related_name='plasmodium_north_direction_set',
        blank=True,
        null=True
    )
    west = models.ForeignKey(
        Plasmodium,
        on_delete=models.PROTECT,
        related_name='plasmodium_west_direction_set',
        blank=True,
        null=True
    )
    east = models.ForeignKey(
        Plasmodium,
        on_delete=models.PROTECT,
        related_name='plasmodium_east_direction_set',
        blank=True,
        null=True
    )
    south = models.ForeignKey(
        Plasmodium,
        on_delete=models.PROTECT,
        related_name='plasmodium_south_direction_set',
        blank=True,
        null=True
    )

    class Meta:
        db_table = 'plasmodium_directions'


class MoistChamber(BaseModel):
    """
    """

    name = models.CharField(max_length=64, blank=True)
    code = models.CharField(max_length=16)
    substrate = models.ForeignKey(Substrate, on_delete=models.PROTECT)
    tree_species = models.ForeignKey(Tree, on_delete=models.PROTECT)
    plasmodiums = models.ForeignKey(
        PlasmodiumDirections,
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )
    fruiting_bodies = models.ForeignKey(
        FruitingBodyDirections,
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )

    class Meta:
        db_table = 'moist_chambers'
