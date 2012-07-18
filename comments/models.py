from django.db import models
from catalog.models import Product


class Comments(models.Model):
         comment= models.TextField()
         name= models.CharField(max_length=50)
         score= models.DecimalField(blank=True,default=0,max_digits=4, decimal_places=1)
         add_time=models.DateTimeField(auto_now=True)
         p=models.CharField(max_length=50)
         class Meta:
           db_table='comments'
		 
         def __unicode__(self):
            return self.name		 


