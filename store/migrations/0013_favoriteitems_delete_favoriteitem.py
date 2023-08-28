# Generated by Django 4.2.4 on 2023-08-25 01:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("store", "0012_remove_favoriteitem_product_favoriteitem_category_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="FavoriteItems",
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
                ("name", models.CharField(max_length=60)),
                ("price", models.IntegerField(default=0)),
                (
                    "description",
                    models.CharField(blank=True, default="", max_length=250, null=True),
                ),
                ("image", models.ImageField(upload_to="")),
                (
                    "category",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="store.category",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="FavoriteItem",
        ),
    ]
