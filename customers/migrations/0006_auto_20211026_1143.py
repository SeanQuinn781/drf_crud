# Generated by Django 3.2.8 on 2021-10-26 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0005_auto_20211026_1139'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='code',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='title',
        ),
    ]
