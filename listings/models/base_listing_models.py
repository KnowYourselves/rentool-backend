# django
from django.db import models
from django.utils.translation import gettext_lazy as _

from base.models import BaseModel
from base.models import file_path


class BaseListing(BaseModel):
    class Status(models.IntegerChoices):
        UNPUBLISHED = 0, _("Unpublished")
        PUBLISHED = 1, _("Published")
        RENTED = 2, _("Rented")

    name = models.CharField(
        verbose_name=_("tool name"),
        max_length=200,
    )
    description = models.TextField(
        verbose_name=_("listing description"),
    )
    image = models.ImageField(
        verbose_name=_("listing image"),
        upload_to=file_path,
    )
    price = models.IntegerField(
        verbose_name=_("tool price"),
    )
    status = models.CharField(
        verbose_name=_("listing status"),
        choices=Status.choices,
        default=Status.PUBLISHED,
        max_length=200,
    )

    class Meta:
        abstract = True
