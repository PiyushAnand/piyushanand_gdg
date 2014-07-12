__author__ = 'owner'
from django.shortcuts import render,render_to_response
from django.template import RequestContext

def home(request):
    templatename='index.html'
    return render_to_response(templatename,{},context_instance=RequestContext(request))