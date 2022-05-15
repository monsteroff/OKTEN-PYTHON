from rest_framework.serializers import ModelSerializer

from apps.cars.models import CarModel


class CarSerializer(ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('id', 'brand', 'price', 'year')
        # fields = '__all'  # hamisini yoxlayacagimizi bele qeyd ede bilerik



