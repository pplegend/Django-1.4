from __future__ import division 
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from iStore.rate.models import *
#from iStore.catalog.views import *
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required

#@login_required
def addRating(request):
      productId=request.GET.get('productid')
      rate=request.GET.get('rate')
      p=Rate.objects.get(p=productId)
      p.votes=p.votes+1#vote times, every time plus one
      p.score=p.score+int(rate)
      p.save()
      ava=int(round(p.score / p.votes,0))
      res=p.votes,',',ava
      response = HttpResponse(res)
      return response
		    