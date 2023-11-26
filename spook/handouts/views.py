from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def formpage(request):
    return HttpResponse("This is where a form page will show")