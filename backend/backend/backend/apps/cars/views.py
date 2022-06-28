from cars.models import Car, CarMake
from cars.serializers import CarSerializer, CarMakeSerializer
from rest_framework.generics import ListAPIView


class CarMakeListAPIView(ListAPIView):
    queryset = CarMake.objects.all()
    serializer_class = CarMakeSerializer

class CarListAPIView(ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    