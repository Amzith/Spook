# Text object, should be printable over an image
class Text:
    def __init__(self, font, position, textContent, colour, styling):
        self.font = font
        self.position = position
        self.textContent = textContent
        self.colour = colour
        self.styling = styling
