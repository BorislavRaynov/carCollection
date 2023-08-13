from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator
from .validators import check_valid_year
# Create your models here.

class Car(models.Model):
    CHOISES = (
        ("Sports Car", "Sports Car"),
        ("Pickup", "Pickup"),
        ("Crossover", "Crossover"),
        ("Minibus", "Minibus"),
        ("Other", "Other")
    )

    type = models.CharField(
        max_length=10,
        choices=CHOISES,
        null=False,
        blank=False
    )

    model = models.CharField(
        max_length=10,
        validators=[MinLengthValidator(2)],
        null=False,
        blank=False
    )

    year = models.IntegerField(
        validators=[check_valid_year],
        null=False,
        blank=False
    )

    image = models.URLField(
        null=False,
        blank=False
    )

    price = models.FloatField(
        validators=[MinValueValidator(1)],
        null=False,
        blank=False
    )
