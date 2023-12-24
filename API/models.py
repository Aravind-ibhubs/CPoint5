from django.db import models

# Create your models here.
class Glocery(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=8,decimal_places=2)
    