# others libraries
from rest_framework import serializers

from listings.models import PastToolListing
from listings.serializers.base_tool_listing_serializer import BaseToolListingSerializer


class PastToolListingSerializer(BaseToolListingSerializer):
    renter = serializers.PrimaryKeyRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault(),
    )

    class Meta:
        model = PastToolListing
        fields = "__all__"

    def save(self, **kwargs):
        kwargs["renter"] = self.fields["renter"].get_default()
        return super().save(**kwargs)
