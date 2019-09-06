import uuid
from django.db import models


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=30)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    photo = models.ImageField(blank=True)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.id)


class Tag(models.Model):
    product = models.ManyToManyField(Product)
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name

