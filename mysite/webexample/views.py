from django.shortcuts import render
from django.http import HttpResponse

def max1 (request):
    return HttpResponse("<h3> Привет Максим!</h3>")
# Create your views here.
