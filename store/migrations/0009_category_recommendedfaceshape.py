# Generated by Django 4.2.4 on 2023-08-21 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0008_category_recommendedgender_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="recommendedFaceShape",
            field=models.CharField(default="Oval", max_length=100),
            preserve_default=False,
        ),
    ]
