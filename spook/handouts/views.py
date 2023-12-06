from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import HandoutForm

import os

# Importing the PIL library
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
 

# Create your views here.
def formpage(request):

    # Handle Form 
    if request.method == "POST":
        form = HandoutForm(request.POST)

        if form.is_valid():
            output_text = form.cleaned_data["contents_text"]
            imagedraw(output_text)
            return render(request, 'output.html', {"output_text":output_text})
    
    else:
        form = HandoutForm()

    context = {
        'title': 'Handouts',
        'date': 1920,
        "form": form
    }

    return render(request, 'home.html', context=context)

# Draw Handout image
def imagedraw(output_text):

    my_img = os.path.abspath("handouts\static\images\paper.jpg")
    # Open an Image
    img = Image.open(my_img)
    
    # Call draw Method to add 2D graphics in an image
    I1 = ImageDraw.Draw(img)
    
    # Custom font style and font size
    myFont = ImageFont.truetype("arial.ttf", 90)
    
    # Add Text to an image
    I1.text((250, 300), output_text, fill =(0, 0, 0))
    
    # Display edited image
    img.show()

    output_img = os.path.abspath("handouts\static\images\output.jpg")
    
    # Save the edited image
    img.save(output_img)