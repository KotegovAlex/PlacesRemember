# Generated by Django 4.2.1 on 2023-05-31 16:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("placesremember_app", "0003_place_lat_place_lon"),
    ]

    operations = [
        migrations.AlterField(
            model_name="place",
            name="photo",
            field=models.ImageField(
                blank=True,
                upload_to="photos/",
                verbose_name="Place Photo",
            ),
        ),
    ]
