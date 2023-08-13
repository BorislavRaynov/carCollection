from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator

# Create your models here.

class Profile(models.Model):

    username = models.CharField(
        max_length=10,
        validators=[MinLengthValidator(2, 'The username must be a minimum of 2 chars')],
        null=False,
        blank=False
    )

    email = models.EmailField(
        null=False,
        blank=False
    )

    age = models.IntegerField(
        validators=[MinValueValidator(18)],
        null=False,
        blank=False
    )

    password = models.CharField(
        max_length=30,
        null=False,
        blank=False
    )

    first_name = models.CharField(
        max_length=30,
        null=True,
        blank=True
    )

    last_name = models.CharField(
        max_length=30,
        null=True,
        blank=True
    )

    picture = models.URLField(
        null=True,
        blank=True
    )
