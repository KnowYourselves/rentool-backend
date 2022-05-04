# django
from django.conf import settings
from django.core import validators
from django.db import models
from django.utils.translation import gettext_lazy as _

from base.models import BaseModel


class Review(BaseModel):
    reviewer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="reviews",
    )
    listing = models.ForeignKey(
        "listings.ToolListing",
        verbose_name=_("listing"),
        related_name="reviews",
        on_delete=models.CASCADE,
    )
    score = models.SmallIntegerField(
        default=0,
        validators=[
            validators.MinValueValidator(1),
            validators.MaxValueValidator(5),
        ],
    )
    description = models.TextField(
        verbose_name=_("description"),
    )
