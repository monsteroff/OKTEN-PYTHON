from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.cars.models import CarModel
from apps.cars.serializers import CarSerializer


class CarListCreateView(APIView):
    def get(self, *args, **kwargs):
        cars = CarModel.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = CarSerializer(data=data)
        # new_car = CarModel.objects.create(**data)
        # return Response({'id': new_car.id, 'brand': new_car.brand, 'price': new_car.price, 'year': new_car.year})

        # if not serializer.is_valid():
        #     return Response(serializer.errors)

        serializer.is_valid(raise_exception=True)

        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class ReadUpdateDeleteView(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        if not CarModel.objects.filter(pk=pk).exists():
            return Response('Car with this id does not exist', status.HTTP_404_NOT_FOUND)
        car = CarModel.objects.get(pk=pk)
        serializer = CarSerializer(car)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        pk = kwargs.get('pk')
        data = self.request.data

        if not CarModel.objects.filter(pk=pk).exists():
            return Response('Car with this id does not exist', status.HTTP_404_NOT_FOUND)
        car = CarModel.objects.get(pk=pk)
        serializer = CarSerializer(car, data=data)

        # if not serializer.is_valid():
        #     return Response(serializer.errors)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, *args, **kwargs):
        pk = kwargs.get('pk')
        data = self.request.data

        if not CarModel.objects.filter(pk=pk).exists():
            return Response('Car with this id does not exist', status.HTTP_404_NOT_FOUND)

        car = CarModel.objects.get(pk=pk)
        serializer = CarSerializer(car, data=data, partial=True)

        # if not serializer.is_valid():
        #     return Response(serializer.errors)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, *args, **kwargs):
        pk = kwargs.get('pk')
        data = self.request.data

        if not CarModel.objects.filter(pk=pk).exists():
            return Response('Car with this id does not exist', status.HTTP_404_NOT_FOUND)

        car = CarModel.objects.get(pk=pk)
        car.delete()
        # return Response('Deleted', status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_204_NO_CONTENT)








