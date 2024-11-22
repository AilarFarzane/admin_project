from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER_TYPES = (
        ('admin', 'Admin'),
        ('user', 'User'),
    )
    role = models.CharField(choices=USER_TYPES, default='user', max_length=50)
    username = models.CharField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=50)


