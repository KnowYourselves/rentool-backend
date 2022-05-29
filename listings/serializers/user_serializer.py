from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
            "groups",
            "phone_number",
        )
