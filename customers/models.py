from django.db import models


class Customer(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=25, default='first_name')
    last_name = models.CharField(max_length=25, default='last_name')

    class Meta:
        ordering = ['created']
