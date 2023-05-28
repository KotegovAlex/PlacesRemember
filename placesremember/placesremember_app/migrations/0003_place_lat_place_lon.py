# Generated by Django 4.2.1 on 2023-05-27 14:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("placesremember_app", "0002_alter_place_user_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="place",
            name="lat",
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name="place",
            name="lon",
            field=models.FloatField(default=0.0),
        ),
    ]