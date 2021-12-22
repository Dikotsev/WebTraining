from django.contrib.auth import get_user_model

from django.db import models

UserModel = get_user_model()
# Create your models here.
class Profile(models.Model):
    first_name = models.CharField(
        max_length=10,
    )
    last_name = models.CharField(
        max_length=10,
        blank=True,
    )
    age = models.ImageField(
        blank=True,
        null=True,

    )
    profile_image = models.ImageField(
        upload_to='media/images',
        blank=True,
    )

    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
        name='id',

    )
    is_complete = models.BooleanField(
        default=False,
    )

from .signals import *