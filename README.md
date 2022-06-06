# OCR-Microservice

Service that can recognize text and formulas from images

## Requirements
- [Tesseract](https://github.com/tesseract-ocr/tesseract)
- [pip-requirements](https://github.com/StudyForces/OCR-Subsystem/blob/498d7afcd57be4d82c81ee4b1f7b30f7322a9804/pip-requirements.txt)

## Usage
All images must be in .png format.

Set the parameters in rmq_parameters.py

- SENDER_QUEUE_NAME - name of the queue to be used as output
- CONSUMER_QUEUE_NAME - name of the queue to be used as input
- HOST - URL for connecting to RabbitMQ

Then run the following command

	python rmq_communication.py
