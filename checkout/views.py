# Create your views here.
from iStore.cart import cart
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from iStore.cart.models import *
import md5

@login_required
def check_out(request,template_name="checkout/checkout.html"):
    payment_id=cart._cart_id(request)
    name = request.user.username
    cart_items=CartItem.objects.filter(cart_id=payment_id)
    amount=0
    for cart_item in cart_items: 
        p=CartItem.total(cart_item)
        amount=amount+p
		
    sid="zhangyongzhen"
    #amount=3
    secret_key="a6ef8c8abf2a4cc6c3bf8fbee71a0504"
    str="pid=%s&sid=%s&amount=%s&token=%s"%(payment_id, sid, amount, secret_key)
    m=md5.new(str)
    checksum=m.hexdigest()
    confirm_checksum="pid=%s&ref=%s&token=%s"%(payment_id, 488, secret_key)
    return render_to_response(template_name, locals(),context_instance=RequestContext(request))