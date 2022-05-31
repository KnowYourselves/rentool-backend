# django
from django.conf import settings
from django.db import models
from django.forms.models import model_to_dict

from listings.models import BaseListing


class PastToolListing(BaseListing):
    renter = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="rented_listings",
    )
    listing = models.ForeignKey(
        "listings.ToolListing",
        on_delete=models.CASCADE,
        related_name="past_listings",
    )

    @classmethod
    def create_from_listing(cls, listing, renter):
        return cls.objects.create(
            **model_to_dict(
                listing,
                exclude=(
                    "id",
                    "publisher",
                ),
            ),
            renter=renter,
            listing=listing,
        )
