# others libraries
from rest_framework import serializers

from listings.models import ListingComplaint


class ListingComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListingComplaint
        fields = "__all__"
        extra_kwargs = {
            "user_receiver": {"required": True},
            "user_complainer": {"required": True},
        }
