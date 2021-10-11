from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Image


# Create your views here.
def index(request):

    photos=Image.get_photos()

    return render(request,'index.html',{"photos":photos})

