# Generated by Django 3.2.8 on 2021-10-27 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0007_customer_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.EmailField(default='test@testing123.com', max_length=100),
        ),
    ]
