# Importing the PIL library
from PIL import ImageFont, Image, ImageDraw
from matplotlib import font_manager

from django.conf import settings

# Service to handle drawing handout images
class ImageDrawService:
    def draw(self, handout):
        img_path = settings.BASE_DIR / 'handouts' / 'static' / 'images'
        background_img_path = img_path / handout.backgroundImage.path

        # Open an Image
        background_img = Image.open(background_img_path)

        # Resize Image, and text wrap each line
        background_img = background_img.resize(handout.backgroundImage.size)
        width, height = background_img.size

        
        # Call draw Method to add 2D graphics in an image
        I1 = ImageDraw.Draw(background_img)

        for text in handout.texts:
            self.drawText(text, I1, width)

        output_file_name = handout.name + '.jpg'
        output_img = img_path / output_file_name

        # Save the edited image
        background_img.save(output_img)

    def drawText(self, text, I1, width):
        # Adding custom font
        font_path = settings.BASE_DIR / 'handouts' / 'static' / 'fonts' / text.font
        font_manager.fontManager.addfont(font_path)
        font = font_manager.FontProperties(fname=font_path)
        file = font_manager.findfont(font)

        title_font = ImageFont.truetype(file, 50)

        all_words = text.textContent.split(' ')

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

        #TODO needs to print the textContent at the given position
        #I1.text(text.position, name_text, (0, 0, 0), font=title_font)

        position = text.position
        for line in all_lines:
            I1.text(position, line, text.colour, align='center', font=title_font)
            position = (position[0], position[1] + 100)