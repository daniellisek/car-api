from cars.models import CarMake, Car
from rest_framework import serializers


class CarMakeSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarMake
        fields = (
            'id', 'make_name', 'is_premium'
        )


class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = (
            'id', 'make', 'model', 'year', 'price'
        )
