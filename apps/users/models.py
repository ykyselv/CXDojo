from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    first_name = models.CharField("first_name", help_text="first_name", max_length=255)
    last_name = models.CharField("last_name", help_text="last_name", max_length=255)
    password = models.CharField("password", help_text="password", max_length=255)
    date_joined = models.DateField(null=True)
