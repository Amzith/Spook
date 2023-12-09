import sys

sys.path.insert(0,"..")

from ..domain.Text import *
from ..domain.Handout import *
from ..domain.Image import *

def createHandout(form):

    output_text = form.cleaned_data["contents_text"]
    name_text = form.cleaned_data["full_name"]

    #TODO: needs to generate two text objects,
    # one with the name field of the form one for the content - ideally it should also position the text correctly
    handout_text = Text('Tangerine-Regular.ttf', (20, 100), output_text, (0, 0, 0), None)
    background_image = BackgroundImage('paper', (1080,1080), 'paper.jpg')
    handout = Handout("output", background_image)

    handout.addText(handout_text)

    return handout
