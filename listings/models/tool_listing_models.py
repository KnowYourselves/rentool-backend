# django
from django.conf import settings
from django.db import models

from listings.models import BaseListing


class ToolListing(BaseListing):
    publisher = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
