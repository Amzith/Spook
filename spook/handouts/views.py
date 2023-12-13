from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import HandoutForm
from .src.services.ImageDrawService import *
from .src.services.HandoutFactory import *

import os

from django.conf import settings

# Importing the PIL library
from PIL import ImageFont, Image, ImageDraw
from matplotlib import font_manager

# Create your views here.
def formpage(request):

    # Handle Form 
    if request.method == "POST":
        form = HandoutForm(request.POST)

        if form.is_valid():

            handout = createHandout(form)

            drawservice = ImageDrawService()
            
            drawservice.draw(handout)
            
    else:
        form = HandoutForm()

    
    context = {
        'title': 'Handouts',
        'date': 1920,
        "form": form
    }
       
    return render(request, 'home.html', context=context)