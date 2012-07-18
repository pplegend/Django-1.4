from django.contrib.auth.forms import UserCreationForm
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.core import urlresolvers
from django.http import HttpResponseRedirect
from iStore.checkout.models import Order, OrderItem
from django.contrib.auth.decorators import login_required
from iStore.accounts.forms import UserProfileForm
from iStore.accounts import profile
from iStore.cart import cart
from django.contrib.auth import logout
from django.contrib.auth import login
def register(request, template_name="registration/register.html"):
     if request.method == 'POST':
       postdata = request.POST.copy()
       form = UserCreationForm(postdata)
       if form.is_valid():
           form.save()
           un = postdata.get('username','')
           pw = postdata.get('password1','')
           from django.contrib.auth import login, authenticate
           new_user = authenticate(username=un, password=pw)
           if new_user and new_user.is_active:
              login(request, new_user)
              url = urlresolvers.reverse('my_account')
              return HttpResponseRedirect(url)
     else:
          form = UserCreationForm()
     page_title = 'User Registration'
     return render_to_response(template_name, locals(),context_instance=RequestContext(request))
	 
	 
@login_required
def logout_view(request, template_name="registration/logged_out.html"):
	 temp_session=cart._cart_id(request)
	 logout(request)
	 request.session[cart.CART_ID_SESSION_KEY]=temp_session
	 return render_to_response(template_name, locals(),context_instance=RequestContext(request))
	 


	 
@login_required
def my_account(request, template_name="registration/my_account.html"):
     page_title = 'My Account'
     orders = Order.objects.filter(user=request.user)
     name = request.user.username
     return render_to_response(template_name, locals(),context_instance=RequestContext(request))
	 
	 
	 
@login_required
def order_details(request, order_id, template_name="registration/order_details.html"):
	order = get_object_or_404(Order, id=order_id, user=request.user)
	order_items = OrderItem.objects.filter(order=order)
	return render_to_response(template_name, locals(),context_instance=RequestContext(request))
	
@login_required
def order_info(request, template_name="registration/order_info.html"):
	if request.method == 'POST':
		postdata = request.POST.copy()
		form = UserProfileForm(postdata)
		if form.is_valid():
			profile.set(request)
			url = urlresolvers.reverse('my_account')
			return HttpResponseRedirect(url)
	else:
		user_profile = profile.retrieve(request)
		form = UserProfileForm(instance=user_profile)
		page_title = 'Edit Order Information'
	return render_to_response(template_name, locals(),context_instance=RequestContext(request))