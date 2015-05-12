from django.shortcuts import render

from models import Pin, Category, Board
# Create your views here.

def index(request):
    context_dict = {}
    pins = Pin.objects.all()[:25]
    context_dict['pins'] = pins
    return render(request, 'pinterest/index.html',context_dict)