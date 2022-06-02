# OCR-Subsystem

Service that can recognize text and formulas from images

## Requirements
- [Tesseract](https://github.com/tesseract-ocr/tesseract)
- [pip-requirements](https://github.com/StudyForces/OCR-Microservice/blob/498d7afcd57be4d82c81ee4b1f7b30f7322a9804/pip-requirements.txt)

## Usage
All images must be in .png format
### Text recognition:
Run the following command

	python get_text.py [< input] [> output]

In the case of using standard I/O, you will have to enter the path to the image
