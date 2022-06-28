from django.contrib import admin
from cars.models import CarMake, Car

# Register your models here.
admin.site.register(CarMake)
admin.site.register(Car)