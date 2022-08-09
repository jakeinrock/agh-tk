import sys
import os

dir = os.path.dirname(os.getcwd())
sys.path.insert(1, dir)

from PythonServicesConfig.main import ConnectToChannel
from utils import create_typos

if __name__ == "__main__":

    log_name = "wordsTypos"
    exchange = 'words'
    host = 'rabbitmq'
    queue = 'words.typos'
    mode = create_typos

    ConnectToChannel(log_name, exchange, host, queue, mode)
