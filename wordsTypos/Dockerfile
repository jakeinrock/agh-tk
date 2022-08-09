FROM python:3.10-slim-buster

RUN mkdir -p /PythonServicesConfig

COPY ./PythonServicesConfig ./PythonServicesConfig

RUN mkdir -p /wordsTypos

WORKDIR /wordsTypos

COPY ./wordsTypos .

COPY ./wordsTypos/requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt

CMD ["python", "run.py"]
