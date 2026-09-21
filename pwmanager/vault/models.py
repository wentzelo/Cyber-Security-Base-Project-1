from cryptography.fernet import Fernet
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

_fernet = Fernet(settings.FERNET_KEY)


def encrypt_password(plain_text):
    return _fernet.encrypt(plain_text.encode()).decode()


def decrypt_password(token):
    return _fernet.decrypt(token.encode()).decode()


class Entry(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='entries')
    site_url = models.CharField(max_length=500)
    password = models.CharField(max_length=500)

    def __str__(self):
        return self.site_url