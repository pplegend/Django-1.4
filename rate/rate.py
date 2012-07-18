from django.http import HttpResponse
from iStore.catalog.models import Product 
from django.core import serializers

def get_json_products(request):
     products=Product.active.all()
	 json_products=serializers.serialize("json",products)
	 return HttpResponse(json_products,content_type='application/javascript; charset=utf-8')