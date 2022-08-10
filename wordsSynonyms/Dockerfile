FROM python:3.10-slim-buster

RUN mkdir -p /PythonServicesConfig

COPY ./PythonServicesConfig ./PythonServicesConfig

RUN mkdir -p /wordsSynonyms

WORKDIR /wordsSynonyms

COPY ./wordsSynonyms .

COPY ./wordsSynonyms/requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt

CMD ["python", "run.py"]
