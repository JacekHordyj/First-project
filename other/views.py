from django.shortcuts import render
from django.http import  HttpResponse

def simple_view(request):
    return HttpResponse('HELLO! ignore rules added, another pull,final pull, another test,at')

# Create your views here.
