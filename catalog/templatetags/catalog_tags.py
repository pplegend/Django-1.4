from django import template
from iStore.cart import cart
from iStore.catalog.models import Category, Product
register=template.Library()

@register.inclusion_tag("tags/cart_box.html")
def cart_box(request):
      cart_item_count=cart.cart_distinct_item_count(request)
      return {'cart_item_count': cart_item_count}
  
@register.inclusion_tag("tags/category_list.html")  
def category_list(request_path):
      active_categories=Category.objects.filter(is_active=True)
      return {
              'active_categories':active_categories,
              'request_path':request_path
              }  
      
@register.inclusion_tag("tags/top_sell.html") 
def top_sell_list(request_path):
      top_sell_products=Product.objects.all().order_by('?')[:6]
      return {
              'topsells':top_sell_products
              } 