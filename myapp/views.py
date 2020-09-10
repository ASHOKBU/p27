from django.shortcuts import render,redirect
from django.http import HttpResponse
from myapp.models import *
# Create your views here.
def display_topics(request):
    topics=Topic.objects.all()
    return render(request,'display_topic.html', context={'topics': topics})
def display_topic(request,id):
    topics=Topic.objects.filter(id=id)
    return render(request,'display_topic.html', context={'topics': topics})
def display_webpages(request):
    webpages=Webpage.objects.all()
    return render(request,'display_webpage.html', context={'webpages':webpages})
def display_webpage(request,webid):
    webpages=Webpage.objects.filter(id=webid)
    return render(request,'display_webpage.html', context={'webpages':webpages})
def search_webpage(request):
    if request.GET.get('search'):
        id= request.GET['search']
        return redirect('display_webpage',webid=id)
    return render(request,'search_webpage.html')