from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=50,decimal_places=2)
    currency = models.CharField(max_length=20,
    choices=(('usd','$'),('rub','₽')),default='usd'
    )

    def __str__(self) -> str:
        return self.name
