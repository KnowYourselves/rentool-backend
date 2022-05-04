# django
from django.db import models
from django.utils.translation import gettext_lazy as _


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
