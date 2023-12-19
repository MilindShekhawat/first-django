# Generated by Django 5.0 on 2023-12-19 05:44

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
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
                ("title", models.CharField(max_length=200)),
                ("text", models.TextField()),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                ("published_at", models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
