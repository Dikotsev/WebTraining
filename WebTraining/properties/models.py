from django.db import models


# Create your models here.
from WebTraining.properties.Properties_utils.validators import price_validator


class Properties(models.Model):

    name = models.CharField(
        max_length=30
    )
    description = models.CharField(
        max_length=100
    )

    price = models.FloatField(
       #validators=price_validator()
    )


class Image(models.Model):
    image = models.ImageField(
       upload_to='images'
    )


class UpdateProperty(Properties):
    pass