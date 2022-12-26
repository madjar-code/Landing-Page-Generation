from django.db import models
from common.models import *


class Template(UUIDModel, TimeStampedModel):

    PREFIX = 'templates/'
    PREFIX2 = 'css/'

    name = models.CharField(max_length=255)
    html_template = models.FileField(upload_to=PREFIX, blank=True)
    template_styles = models.FileField(upload_to=PREFIX2, blank=True)

    class Meta:
        verbose_name = 'Шаблон'
        verbose_name_plural = 'Шаблоны'

    def get_file_name(self) -> str:
        template_path = str(self.html_template)
        prefix_length = len(Template.PREFIX)
        file_name = template_path[prefix_length:]
        return file_name

    def __str__(self) -> str:
        return self.name
