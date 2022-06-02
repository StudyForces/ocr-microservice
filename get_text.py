from PIL import Image
import pytesseract
import cv2
import os
import sys
 
# all images must be in .png format

def preprocessing(image):
    img = cv2.imread(image, 0)
    _, res = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return res

def get_text(img_filename, temp_filename="temp.png"):
    cv2.imwrite(temp_filename, preprocessing(img_filename))
    text = pytesseract.image_to_string(Image.open(temp_filename),
                                       lang='rus',
                                       output_type=pytesseract.Output.STRING)
    return text

def main():
    img_filename = sys.stdin.readline().rstrip()
    res = get_text(img_filename)
    sys.stdout.write(res)
    return 0

if __name__ == "__main__":
    main()


