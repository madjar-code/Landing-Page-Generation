from django.db import models
from offer.models import Offer
from web_templates.models import Template
from common.models import *


class Web(UUIDModel, TimeStampedModel):
    name = models.CharField(max_length=255)
    domain = models.CharField(max_length=255)
    character_code = models.CharField(max_length=255)
    html_code = models.TextField()
    url = models.URLField(max_length=255)
    ref_url = models.URLField(max_length=255)
    template = models.ForeignKey(
        to=Template, 
        on_delete=models.PROTECT,
        null=True)

    offers = models.ManyToManyField(
        verbose_name='Предложения',
        to=Offer, null=True)

    class Meta:
        verbose_name = 'Веб'
        verbose_name_plural = 'Вебы'


    def __str__(self) -> str:
        return self.name