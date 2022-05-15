from django.urls import path

from apps.cars.views import CarListCreateView, ReadUpdateDeleteView

urlpatterns = [
    # localhost:8000/cars
    path('', CarListCreateView.as_view(), name='cars_list_create'),
    # localhost:8000/cars/1
    path('<int:pk>/', ReadUpdateDeleteView.as_view(), name='cars_read_update_delete')  # pk -> primary key
]
