# others libraries
from rest_framework import serializers

from listings.models import ToolListing


class ToolListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToolListing
        fields = "__all__"
