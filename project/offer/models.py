from django.db import models
from common.models import *


class Offer(UUIDModel, TimeStampedModel):

    LOGO_PREFIX = 'logos'

    logo = models.ImageField(
        verbose_name='Логотип',
        upload_to=LOGO_PREFIX, blank=True)
    name = models.CharField(verbose_name='Название',max_length=255)
    # logo = models.ImageField(to=)
    sum = models.BigIntegerField(verbose_name='Сумма')
    rate = models.DecimalField(
        verbose_name='Ставка', max_digits=4, decimal_places=2)
    minimum_term = models.PositiveIntegerField(verbose_name='Минимальный срок')
    maximum_term = models.PositiveIntegerField(verbose_name='Максимальный срок')
    url = models.URLField(verbose_name='Ссылка', max_length=255, blank=True)

    def get_interest_rate(self) -> float:
        result = self.rate * 100
        return round(result, 1)

    class Meta:
        verbose_name = 'Оффер'
        verbose_name_plural = 'Офферы'


    def __str__(self) -> str:
        return self.name