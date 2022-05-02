# django
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class ToolListing(models.Model):
    class Status(models.IntegerChoices):
        UNPUBLISHED = 0, _("Unpublished")
        PUBLISHED = 1, _("Published")
        TAKEN = 2, _("Taken")

    name = models.CharField(
        verbose_name=_("tool name"),
        max_length=200,
    )
    description = models.TextField(
        verbose_name=_("listing description"),
    )
    image = models.ImageField(
        verbose_name=_("listing image"),
    )
    price = models.IntegerField(
        verbose_name=_("tool price"),
    )
    status = models.CharField(
        verbose_name=_("listing status"),
        choices=Status.choices,
        default=Status.UNPUBLISHED,
        max_length=200,
    )
    publisher = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
