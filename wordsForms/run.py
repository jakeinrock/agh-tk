import sys
import os

dir = os.path.dirname(os.getcwd())
sys.path.insert(1, dir)

from PythonServicesConfig.main import ConnectToChannel
from utils import forms_generator

if __name__ == "__main__":

    ConnectToChannel(
        log_name="wordsForms",
        exchange='words',
        host='rabbitmq',
        queue='words.forms',
        mode=forms_generator,
        )
