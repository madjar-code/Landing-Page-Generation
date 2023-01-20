from django.db import models
from offer.models import Offer
from web_templates.models import Template
from common.models import *


class Web(UUIDModel, TimeStampedModel):
    name = models.CharField(verbose_name='Имя', max_length=255)
    domain = models.CharField(verbose_name='Домен', max_length=255, blank=True, null=True)
    character_code = models.CharField(
        verbose_name='Символьный код', max_length=255,
        blank=True, null=True)

    html_code = models.TextField(verbose_name='HTML-код', blank=True)
    url = models.URLField(
        verbose_name='URL для возврата на другую страницу',
        max_length=255, blank=True)
    ref_url = models.URLField(
        verbose_name='Ref URL', max_length=255)

    template = models.ForeignKey(
        to=Template, 
        on_delete=models.PROTECT,
        null=True)
    offers = models.ManyToManyField(
        verbose_name='Предложения',
        to=Offer, null=True, blank=True)

    class Meta:
        verbose_name = 'Веб'
        verbose_name_plural = 'Вебы'


    def __str__(self) -> str:
        return self.name