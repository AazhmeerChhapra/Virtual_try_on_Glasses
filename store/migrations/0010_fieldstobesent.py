# Generated by Django 4.2.4 on 2023-08-24 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0009_category_recommendedfaceshape"),
    ]

    operations = [
        migrations.CreateModel(
            name="FieldsToBeSent",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("number", models.IntegerField()),
            ],
        ),
    ]