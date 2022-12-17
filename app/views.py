from django.shortcuts import render

# Create your views here.
from app.models import *
from django.db.models.functions import Length

def Topic_display(request):
  LTO=Topic.objects.all()
  d={'LTO':LTO}
  return render(request,'Topic_display.html',d)

def Webpage_display(request):
  LWO=Webpage.objects.all()
  d={'LWO':LWO}
  return render(request,'Webpage_display.html',d)

def Access_display(request):
  LAO=Access.objects.all()
  d={'LAO':LAO}
  return render(request,'Access_display.html',d)

def update_Webpage(request):
  LWO=Webpage.objects.all()
  LWO=Webpage.objects.all().order_by(Length('Name'))
  LWO=Webpage.objects.all().order_by(Length('Name').desc())
  #Webpage.objects.filter(Topic_Name='boxing').update(Name='BROCK')
  Webpage.objects.filter(Topic_Name='boxing').update(URL='https://BROCK.in')
  T=Topic.objects.get_or_create(Topic_Name='cricket')[0]
  T.save()
  Webpage.objects.update_or_create(Name='ABD',defaults={'Topic_Name':T,'URL':'https://ABD.in'})
  Webpage.objects.update_or_create(Name='Miler',defaults={'Topic_Name':T,'URL':'https://Miler.in'})
  d={'LWO':LWO}
  return render(request,'Webpage_display.html',d)