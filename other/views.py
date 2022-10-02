from django.shortcuts import render
from django.http import  HttpResponse

def simple_view(request):
    return HttpResponse('HELLO!')

# Create your views here.
