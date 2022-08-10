FROM python:3.10-slim-buster

RUN mkdir -p /PythonServicesConfig

COPY ./PythonServicesConfig ./PythonServicesConfig

RUN mkdir -p /converter

WORKDIR /converter

COPY ./converter/create_connect.py ./create_connect.py
COPY ./converter/run.py ./run.py

COPY ./converter/requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
RUN apt update && apt install -y ffmpeg && rm -rf /var/lib/apt/lists/*

# Samples
COPY ./converter/samples/eng.mp3 /home/converter/samples/
COPY ./converter/samples/pl.mp3 /home/converter/samples/

ENTRYPOINT ["python", "run.py"]
