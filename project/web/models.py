from django.db import models
from common.models import UUIDModel, TimeStampedModel


class Web(UUIDModel, TimeStampedModel):
    name = models.CharField(max_length=255)
    domain = models.CharField(max_length=255)
    character_code = models.CharField(max_length=255)
    html_code = models.TextField()
    url = models.URLField(max_length=255)
    ref_url = models.URLField(max_length=255)

    def __str__(self) -> str:
        return self.name