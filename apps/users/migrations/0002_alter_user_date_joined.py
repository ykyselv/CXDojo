# Generated by Django 4.1 on 2022-10-09 23:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="date_joined",
            field=models.DateField(null=True),
        ),
    ]
