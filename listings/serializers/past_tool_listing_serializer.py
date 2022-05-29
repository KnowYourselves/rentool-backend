# others libraries
from rest_framework import serializers

from listings.models import PastToolListing


class PastToolListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PastToolListing
        fields = "__all__"
