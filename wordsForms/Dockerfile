FROM python:3.10-slim-buster

RUN mkdir -p /PythonServicesConfig

COPY ./PythonServicesConfig ./PythonServicesConfig

RUN mkdir -p /wordsForms

WORKDIR /wordsForms

COPY ./wordsForms .

COPY ./wordsForms/requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt

CMD ["python", "run.py"]
