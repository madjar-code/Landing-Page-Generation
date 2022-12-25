from django.db import models
from common.models import *


class Template(UUIDModel, TimeStampedModel):
    name = models.CharField(max_length=255)
    html_code = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Шаблон'
        verbose_name_plural = 'Шаблоны'

    def __str__(self) -> str:
        return self.name
