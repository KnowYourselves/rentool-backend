# others libraries
from rest_framework import serializers

from listings.models import ToolListing


from drf_extra_fields.fields import Base64ImageField


class UploadedBase64ImageSerializer(serializers.Serializer):
    file = Base64ImageField(required=False)


class ToolListingSerializer(serializers.ModelSerializer):
    publisher = serializers.PrimaryKeyRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault(),
    )

    image = UploadedBase64ImageSerializer()

    class Meta:
        model = ToolListing
        fields = "__all__"

    def save(self, **kwargs):
        kwargs["publisher"] = self.fields["publisher"].get_default()
        return super().save(**kwargs)
