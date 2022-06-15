# standard library
from uuid import uuid4

# django
from django.db import models
from django.utils.translation import gettext_lazy as _

from base import utils


def file_path(instance, name):
    return f"{instance.__class__.__name__}/{utils.today()}/{uuid4()}/{name}"


class BaseModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text=_("creation date"),
        verbose_name=_("created at"),
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        null=True,
        help_text=_("edition date"),
        verbose_name=_("updated at"),
    )

    class Meta:
        abstract = True
