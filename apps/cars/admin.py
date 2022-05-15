from django.contrib import admin
from apps.cars.models import CarModel
# Register your models here.


# admin.site.register(CarModel)
# # ya yuxaridaki kimi yada ashagidaki kimi eleye bilerik
@admin.register(CarModel)
class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand', 'price', 'year')
    sortable_by = ('id', 'brand', 'price', 'year')

