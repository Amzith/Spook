import sys

sys.path.insert(0,"..")

from domain.Text import *
from domain.Handout import *

def createHandout(handout, textContent)

    handout_text = Text('Tangerine-Regular.ttf', (20, 100), textContent, (0, 0, 0), null)
    handout = Handout("output", 'paper.jpg')

    handout.addtext(handout_text)

    return handout
