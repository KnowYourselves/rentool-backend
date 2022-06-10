# others libraries
from rest_framework import serializers

from listings.models import ToolListing
from listings.serializers.base_tool_listing_serializer import BaseToolListingSerializer


class ToolListingSerializer(BaseToolListingSerializer):
    publisher = serializers.PrimaryKeyRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault(),
    )

    class Meta:
        model = ToolListing
        fields = "__all__"

    def save(self, **kwargs):
        kwargs["publisher"] = self.fields["publisher"].get_default()
        return super().save(**kwargs)
