from django.db import NotSupportedError
from django.db import models
from django.utils import timezone


class DoerOfActionModel(models.Model):
    """
    Model with fields to record the user id.
    """

    created_by = models.IntegerField()
    modified_by = models.IntegerField()

    class Meta:
        abstract = True


class TimeStampedModel(models.Model):
    """
    Model to track time of audit.
    """

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SoftDeletableModel(models.Model):
    """
    When deleting, the model is only flagged as inactive if
    this is extended by said model.
    """

    is_active = models.BooleanField(default=True)
    deleted_by = models.IntegerField()
    datetime_deleted = models.DateTimeField(blank=True, null=True)

    class Meta:
        abstract = True

    def soft_delete(self, user=None):
        """
        Deactivate user and update deletion-related fields.
        """
        self.datetime_deleted = timezone.now()
        self.deleted_by = user
        self.is_active = False
        self.save(
            update_fields=['datetime_deleted', 'deleted_by', 'is_active']
        )

    def delete(self):
        """
        Override method to avoid accidental deletions.
        """
        raise NotSupportedError()


class BaseModel(DoerOfActionModel, TimeStampedModel, SoftDeletableModel):
    """
    Base model to be used throughout the project.
    """

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.__class__.__name__} #{self.pk}'


class ForeignFileModel(models.Model):
    """
    Designed to store images not through a FileField
    but through a TextField for custom implementations
    of fetching files from storage.
    """

    file_address = models.TextField()

    class Meta:
        abstract = True


class OrderedModel(models.Model):
    """
    Adds a field to be used as metadata for ordering values.
    """

    order = models.IntegerField()

    class Meta:
        abstract = True
