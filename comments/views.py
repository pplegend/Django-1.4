from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from iStore.comments.models import *
#from iStore.catalog.views import *
import json
from django.http import HttpResponse, Http404 
from django.contrib.auth import logout
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


#@login_required	 
def addComments(request):
    if request.method != 'POST':
	     raise Http404('Only POSTs are allowed')
		 
    #if request.session.get('has_commented',True):	 
    productId=request.POST.get('productid')
    score1=request.POST.get('score')
    comments1=request.POST.get('comments')
    name1=request.POST.get('name')
    add_time1=request.POST.get('time')
    b=Comments(comment=comments1,name=name1,score=score1,add_time=add_time1,p=productId)
    b.save()
    res={ "status": "successful","comment":comments1,"score":score1,"name":name1,"add_time":add_time1}
    data=json.dumps(res, indent=4)
    response = HttpResponse(data)
         #request.session['has_commented']= False
    return response	 