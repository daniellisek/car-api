from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
#
# 


class CarMake(models.Model):

    class CarMakeChoices(models.TextChoices):
        AUDI = 'A', _('Audi')
        BMW = 'B', _('BMW')
        TOYOTA = 'T', _('Toyota')
        SKODA = 'S', _('Skoda')

    make_name = models.CharField(max_length=1, choices=CarMakeChoices.choices, default=CarMakeChoices.AUDI)
    is_premium = models.BooleanField(default=False)

    def __str__(self):
        return self.make_name


class Car(models.Model):
    make = models.ForeignKey('cars.CarMake', on_delete=models.CASCADE, related_name='cars')
    model = models.CharField(max_length=200)
    year = models.IntegerField()
    price = models.FloatField()

    def __str__(self):
        return f'{self.model} {self.year}'
