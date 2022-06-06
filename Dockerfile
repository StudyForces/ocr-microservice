FROM python:slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN apt update
RUN apt install -y libsm6 libxext6 ffmpeg libfontconfig1 libxrender1 libgl1-mesa-glx

RUN pip3 install -r requirements.txt

COPY . .

CMD ["python", "/app/rmq_communication.py"]