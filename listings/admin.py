# django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from listings.models.custom_user_model import CustomUser

admin.site.register(CustomUser, UserAdmin)
