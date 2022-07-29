from PIL import Image
import pytesseract
import cv2


# all images must be in .png format

def preprocessing(image: str, c: list = []) -> str:
    """edits the original image\n
       c - cropping, if len(c) = 0 cropping is not required\n
       otherwise len(c) = 4, (x, y, w, h)\n
    """
    img = cv2.imread(image, cv2.IMREAD_UNCHANGED)
    if (len(img.shape) == 3 and img.shape[2] == 4):
        tmask = img[:, :, 3] == 0
        img[tmask] = [255, 255, 255, 255]
    if (len(img.shape) == 3):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    if len(c) != 0:
        img = img[c[1]:c[1] + c[3], c[0]:c[0] + c[2]]
    _, res = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    cv2.imwrite(image, res)
    return image


def get_text(img_filename) -> str:
    text = pytesseract.image_to_string(Image.open(img_filename),
                                       lang='rus',
                                       output_type=pytesseract.Output.STRING)
    return text
