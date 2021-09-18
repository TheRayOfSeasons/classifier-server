from django.db import models

from core.models import BaseModel


class Tree(BaseModel):
    """
    A type of tree for specimens.
    """

    name = models.CharField(max_length=64)

    class Meta:
        db_table = 'trees'
