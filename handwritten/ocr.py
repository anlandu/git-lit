try:
    import Image
except ModuleNotFoundError:
    import PIL.Image
import pytesseract
import sys
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
from wand.image import Image
class GetText:
    def getText(filename):
        return pytesseract.image_to_string(PIL.Image.open(filename))
