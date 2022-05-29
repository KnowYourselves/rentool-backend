from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator


class CustomUser(AbstractUser):
    REQUIRED_FIELDS = ["email", "phone_number"]
    phone_number_regex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phone_number = models.CharField(
        validators=[phone_number_regex], max_length=16, unique=True
    )
