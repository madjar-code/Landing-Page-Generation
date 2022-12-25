import uuid
from django.db import models


class UUIDModel(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)

    class Meta:
        abstract=True


class TimeStampedModel(models.Model):

    is_active = models.BooleanField(verbose_name='Активен', default=True)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True, null=True)
    updated_at = models.DateTimeField(verbose_name='Дата редактирования', auto_now=True, null=True)

    class Meta:
        abstract = True