# Handout object, should contain everything needed to draw an image handout
class Handout:
    def __init__(self, name, background):
        self.name = name
        self.backgroundImage = background
        self.texts = []
        self.images = []

    def addText(self, text):
        self.texts.append(text)

    def addImage(self, image):
        self.images.append(image) 