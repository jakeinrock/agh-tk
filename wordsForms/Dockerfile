FROM python:3.10-slim-buster

RUN mkdir -p /wordsServices_textExtractor_config

COPY ./wordsServices_textExtractor_config ./wordsServices_textExtractor_config

RUN mkdir -p /wordsForms

WORKDIR /wordsForms

COPY ./wordsForms .

COPY ./wordsForms/requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt

CMD ["python", "wordForms_run.py"]
