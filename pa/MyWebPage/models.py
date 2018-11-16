from django.db import models


class BrandType(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    count = models.PositiveIntegerField()
    image = models.ImageField(upload_to='products')
    brand_type = models.ForeignKey(BrandType, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Модели'

