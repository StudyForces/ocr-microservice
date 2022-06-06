# OCR-Microservice

Service that can recognize text and formulas from images

## Requirements
- [Tesseract](https://github.com/tesseract-ocr/tesseract)
- [requirements](https://github.com/StudyForces/ocr-microservice/blob/main/pip-requirements.txt)

## Usage
All images must be in .png format.

Set the parameters in rmq_parameters.py

- SENDER_QUEUE_NAME - name of the queue to be used as output
- CONSUMER_QUEUE_NAME - name of the queue to be used as input
- HOST - URL for connecting to RabbitMQ

Then run the following command

	python rmq_communication.py
