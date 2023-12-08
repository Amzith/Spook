# Image object
class Image:
    def __init__(self, name, size, path):
        self.name = name
        self.size = size
        self.path = path

#Background image, should cover the whole image
class BackgroundImage(Image):
    pass

# Overlay image, needs to be positionable
class OverlayImage(Image):
    def __init__(self, name, size, path, position, scale):
        super(OverlayImage, self).__init__(name,size,path)
        self.position = position
        self.scale = scale