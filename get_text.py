from PIL import Image
import pytesseract


# all images must be in .png format

def preprocessing(image: str, c: list = []) -> str:
    """edits the original image\n
       c - cropping, if len(c) = 0 cropping is not required\n
       otherwise len(c) = 4, (x, y, w, h)\n
    """
    Image.open("temp.png").crop((c[0], c[1], c[0] + c[2], c[1] + c[3])).save(image)
    return image


def get_text(img_filename) -> str:
    text = pytesseract.image_to_string(Image.open(img_filename),
                                       lang='rus',
                                       output_type=pytesseract.Output.STRING)
    return text
