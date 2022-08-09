FROM python:3.10-slim-buster

RUN mkdir -p /PythonServicesConfig

COPY ./PythonServicesConfig ./PythonServicesConfig

RUN mkdir -p /audio_service

WORKDIR /audio_service

COPY ./audio_service/create_connect.py ./create_connect.py
COPY ./audio_service/run.py ./run.py

COPY ./audio_service/requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt

# Samples
COPY ./audio_service/audio_samples/sample_eng.wav /home/audio_service/audio_samples/
COPY ./audio_service/audio_samples/sample_pl.wav /home/audio_service/audio_samples/

CMD ["python", "run.py"]
