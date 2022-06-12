# others libraries
from rest_framework import serializers

from listings.serializers.base64_image_serializer import Base64ImageField


class BaseToolListingSerializer(serializers.ModelSerializer):
    image = Base64ImageField()
