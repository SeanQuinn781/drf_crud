# Generated by Django 3.2.8 on 2021-10-26 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("customers", "0004_auto_20211026_1138"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customer",
            name="language",
        ),
        migrations.RemoveField(
            model_name="customer",
            name="linenos",
        ),
        migrations.RemoveField(
            model_name="customer",
            name="style",
        ),
        migrations.AddField(
            model_name="customer",
            name="first_name",
            field=models.CharField(default="first_name", max_length=25),
        ),
    ]
