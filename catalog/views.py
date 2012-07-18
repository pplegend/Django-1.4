from __future__ import division 
from django.shortcuts import get_object_or_404, render_to_response
from iStore.catalog.models import Category, Product
from django.template import RequestContext
from django.core import urlresolvers
from iStore.cart import cart
from iStore.rate.models import *
from iStore.comments.models import *
from django.http import HttpResponseRedirect
from iStore.catalog.forms import ProductAddToCartForm
#from iStore.catalog.forms import ProductAddToCartForm
from django.http import HttpResponse
import datetime

def index(request, template_name="catalog/index.html"):
      products=Product.objects.all().order_by('?')[:6]
      return render_to_response(template_name, locals(),context_instance=RequestContext(request))
		   
def show_category(request, category_slug, template_name="catalog/category.html"):
     c = get_object_or_404(Category, slug=category_slug)
     products = c.product_set.all()
     page_title = c.name
     meta_keywords = c.meta_keywords
     #meta_description = c.meta_description
     return render_to_response(template_name, locals(),context_instance=RequestContext(request))

	 
def show_product(request, product_slug, template_name="catalog/product.html"):
    p = get_object_or_404(Product, slug=product_slug)
    categories = p.categories.all()
    page_title = p.name
    p_id=p.id
 
    rr=Rate.objects.get_or_create(votes=3,score=9,p_id=p_id)
    r=Rate.objects.get(p_id=p_id)   
    average=int(round(r.score / r.votes,0))
    co=Comments.objects.filter(p=p_id).order_by("-add_time")
    
    		  
    now=datetime.datetime.now()
    meta_keywords = p.meta_keywords
    meta_description = p.meta_description
    description=p.description
    description_short=description[0:250]
    comment_count=co.count()
    # need to evaluate the HTTP method
    if request.method == 'POST':
       postdata = request.POST.copy()
       form = ProductAddToCartForm(request, postdata)
#check if posted data is valid
       if form.is_valid():
#add to cart and redirect to cart page
         cart.add_to_cart(request)
# if test cookie worked, get rid of it
         if request.session.test_cookie_worked():
            request.session.delete_test_cookie()
         url = urlresolvers.reverse('show_cart')
         return HttpResponseRedirect(url)
    else:
     form = ProductAddToCartForm(request=request, label_suffix=':')
# assign the hidden input the product slug
    form.fields['product_slug'].widget.attrs['value'] = product_slug
# set the test cookie on our first GET request
    request.session.set_test_cookie()
    return render_to_response("catalog/product.html", locals(),context_instance=RequestContext(request))
