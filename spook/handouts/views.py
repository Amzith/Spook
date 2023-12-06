from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import HandoutForm

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
            output_text = form.cleaned_data["contents_text"]
            name_text = form.cleaned_data["full_name"]

            imagedraw(output_text, name_text)

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
def imagedraw(output_text, name_text):

    # Adding custom font
    font_path = settings.BASE_DIR / 'handouts' / 'static' / 'fonts' / 'Tangerine-Regular.ttf'
    font_manager.fontManager.addfont(font_path)
    font = font_manager.FontProperties(fname=font_path)
    file = font_manager.findfont(font)

    img_path = settings.BASE_DIR / 'handouts' / 'static' / 'images'
    my_img = img_path / 'paper.jpg'

    # Open an Image
    img = Image.open(my_img)

    # Resize Image, and text wrap each line
    img = img.resize((1080,1080))
    width, height = img.size

    title_font = ImageFont.truetype(file, 50)

    all_words = output_text.split(' ')
    all_lines = []
    line = []
    while all_words:
        word = all_words[0]
        new_text = ' '.join(line + [word])
        if title_font.getlength(new_text) > (width-30):
            all_lines.append(' '.join(line))
            line = []
        else:
            line += [word]
            all_words = all_words[1:]
        
    if line:
        all_lines.append(' '.join(line))  

    
    # Call draw Method to add 2D graphics in an image
    I1 = ImageDraw.Draw(img)
    I1.text((20, 100), name_text, (0, 0, 0), font=title_font)

    y = 250
    for text in all_lines:
        I1.text((20, y), text, (0, 0, 0), align='center', font=title_font)
        y += 100
    
    # Display edited image
    img.show()

    output_img = img_path / 'output.jpg'

    # Save the edited image
    img.save(output_img)