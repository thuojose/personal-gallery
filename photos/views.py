from django.shortcuts import render
from django.http import HttpResponse,Http404
import datetime as dt
from .models import Image


# Create your views here.
def index(request):

    photos=Image.get_photos()

    return render(request,'index.html',{"photos":photos})

def today_photos(request):
    date=dt.date.today()


    return render(request,'all-photos/today-photos.html',{"date":date})
