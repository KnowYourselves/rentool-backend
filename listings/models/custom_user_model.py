from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    REQUIRED_FIELDS = ["username", "email", "phone_number"]
    phone_number = models.CharField(max_length=20, blank=False, null=False)
