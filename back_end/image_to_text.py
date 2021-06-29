from PIL import Image
from pytesseract import image_to_string 

class ImageToText:

    def __init__(self):
        pass

    def convert(self, path = "testocr.png"):
        
        raw_data = image_to_string(Image.open(path),lang='eng')
        f = open("document.txt", "a")
        f.write(raw_data)
        f.close()

        return raw_data
