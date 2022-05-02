# django
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class RentedTool(models.Model):
    listing = models.ForeignKey(
        "listings.ToolListing",
        verbose_name=_("listing"),
        related_name="rented_tools",
        on_delete=models.CASCADE,
    )
    renter = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
    )
