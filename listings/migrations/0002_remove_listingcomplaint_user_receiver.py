# Generated by Django 3.2.13 on 2022-05-23 04:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("listings", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="listingcomplaint",
            name="user_receiver",
        ),
    ]
