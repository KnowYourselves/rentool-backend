# django
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from base.models import BaseModel


class ListingComplaint(BaseModel):
    listing = models.ForeignKey(
        "listings.ToolListing",
        on_delete=models.CASCADE,
        related_name="complaints",
    )
    user_complainer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.SET_NULL,
        related_name="complaints_made",
    )
    description = models.TextField(
        verbose_name=_("complaint description"),
    )
