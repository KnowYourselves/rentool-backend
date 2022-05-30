# others libraries
from rest_framework import serializers

from listings.models import ListingComplaint


class ListingComplaintSerializer(serializers.ModelSerializer):
    user_complainer = serializers.PrimaryKeyRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault(),
    )

    class Meta:
        model = ListingComplaint
        fields = "__all__"
        extra_kwargs = {
            "user_complainer": {"required": True},
        }

    def save(self, **kwargs):
        kwargs["user_complainer"] = self.fields["user_complainer"].get_default()
        return super().save(**kwargs)
