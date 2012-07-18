from django.db import models
from catalog.models import Product
class Rate(models.Model):
         votes= models.PositiveIntegerField(blank=True,default=0)
         score= models.DecimalField(blank=True,default=0,max_digits=4, decimal_places=1)
         p=models.ForeignKey(Product)
         class Meta:
           db_table='rating'
