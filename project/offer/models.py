from django.db import models
from web.models import Web
from common.models import UUIDModel, TimeStampedModel


class Offer(UUIDModel, TimeStampedModel):
    name = models.CharField(verbose_name='Название',max_length=255)
    # logo = models.ImageField(to=)
    sum = models.BigIntegerField(verbose_name='Сумма')
    rate = models.DecimalField(
        verbose_name='Ставка', max_digits=4, decimal_places=2)
    minimum_term = models.PositiveIntegerField(verbose_name='Минимальный срок')
    maximum_term = models.PositiveIntegerField(verbose_name='Максимальный срок')

    web = models.ForeignKey(verbose_name='Веб', to=Web, null=True, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name