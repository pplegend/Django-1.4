from django.shortcuts import render_to_response
from django.template import RequestContext
def home(request):
     return render_to_response("index.html",context_instance=RequestContext(request))

def about(request):
     return render_to_response("navigation/about.html",context_instance=RequestContext(request))

def privacy(request):
     return render_to_response("navigation/privacy.html",context_instance=RequestContext(request))

def projects(request):
     return render_to_response("navigation/projects.html",context_instance=RequestContext(request))

def contacts(request):
     return render_to_response("navigation/contacts.html",context_instance=RequestContext(request))
