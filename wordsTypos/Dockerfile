FROM python:3.10-slim-buster

RUN mkdir -p /wordsServices_textExtractor_config

COPY ./wordsServices_textExtractor_config ./wordsServices_textExtractor_config

RUN mkdir -p /wordsTypos

WORKDIR /wordsTypos

COPY ./wordsTypos .

COPY ./wordsTypos/requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt

CMD ["python", "wordsTypos_run.py"]
