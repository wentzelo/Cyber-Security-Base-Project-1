from django.db import models
from django.contrib.auth.models import User


class Entry(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='entries')
    site_url = models.CharField(max_length=500)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.site_url