# others libraries
from rest_framework import serializers

from listings.models import ToolListing


class ToolListingSerializer(serializers.ModelSerializer):
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


class ToolListingRentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToolListing
        fields = ["id", "status"]

    def validate(self, attrs):
        if self.instance.status == str(ToolListing.Status.RENTED):
            raise serializers.ValidationError("Can't rent an already rented listing")
        return super().validate(attrs)
