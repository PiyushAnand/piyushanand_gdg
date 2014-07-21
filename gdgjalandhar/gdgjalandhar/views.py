__author__ = 'owner'
from django.shortcuts import render,render_to_response
from django.template import RequestContext
from gdgmain.models import menu,banner,social
def home(request):
    templatename='index.html'
    menuobj=menu.objects.all()
    socialobj=social.objects.all()
    bannerobj=banner.objects.all()
    return render_to_response(templatename,{
        'menu':menuobj,
        'social':socialobj[0],
        'banner':bannerobj,
    },context_instance=RequestContext(request))

def about(request):
    templatename='about.html'
    return render_to_response(templatename,{},context_instance=RequestContext(request))

def events(request):
    templatename='event.html'
    return render_to_response(templatename,{},context_instance=RequestContext(request))

def gallery(request):
    templatename='gallery.html'
    return render_to_response(templatename,{},context_instance=RequestContext(request))

def contactus(request):
    templatename='contactus.html'
    return render_to_response(templatename,{},context_instance=RequestContext(request))