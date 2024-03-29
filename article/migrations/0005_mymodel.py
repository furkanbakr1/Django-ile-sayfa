# Generated by Django 4.2 on 2023-06-14 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("article", "0004_alter_article_options_alter_comment_options"),
    ]

    operations = [
        migrations.CreateModel(
            name="MyModel",
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
                ("name", models.CharField(max_length=100)),
                ("image", models.ImageField(upload_to="media/")),
            ],
        ),
    ]
