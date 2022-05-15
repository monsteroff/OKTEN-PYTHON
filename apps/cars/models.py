from django.db import models


class CarModel(models.Model):
    class Meta:
        db_table = 'cars'
        verbose_name = 'Car'

    brand = models.CharField(max_length=30)
    price = models.IntegerField()
    year = models.IntegerField()

    def __str__(self):
        allinfo = f'{self.brand}({str(self.year)}) - {str(self.price)}USD'
        return allinfo
