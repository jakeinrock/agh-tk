FROM python:3.10-slim-buster

RUN mkdir -p /PythonServicesConfig

COPY ./PythonServicesConfig ./PythonServicesConfig

RUN mkdir -p /textExtractor

WORKDIR /textExtractor

COPY ./textExtractor .

COPY ./textExtractor/requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt

CMD ["python", "run.py"]
