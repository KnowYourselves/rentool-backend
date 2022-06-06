# others libraries
from rest_framework import serializers

from listings.models import ToolListing
from serializers.base64_image_serializer import Base64ImageField


class ToolListingSerializer(serializers.ModelSerializer):
    publisher = serializers.PrimaryKeyRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault(),
    )
    image = Base64ImageField()

    class Meta:
        model = ToolListing
        fields = "__all__"

    def save(self, **kwargs):
        kwargs["publisher"] = self.fields["publisher"].get_default()
        return super().save(**kwargs)
