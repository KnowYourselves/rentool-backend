# others libraries
from rest_framework import serializers

from listings.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    reviewer = serializers.PrimaryKeyRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault(),
    )

    class Meta:
        model = Review
        fields = "__all__"
        extra_kwargs = {"reviewer": {"required": True}}

    def save(self, **kwargs):
        kwargs["reviewer"] = self.fields["reviewer"].get_default()
        return super().save(**kwargs)
