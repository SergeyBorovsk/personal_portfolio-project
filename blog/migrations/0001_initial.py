# Generated by Django 4.1.2 on 2022-11-29 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Blogs",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("date_time", models.DateField(auto_now=True)),
                ("description", models.CharField(max_length=250)),
            ],
        ),
    ]
