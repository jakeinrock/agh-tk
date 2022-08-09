import sys
import os

dir = os.path.dirname(os.getcwd())
sys.path.insert(1, dir)

from PythonServicesConfig.main import ConnectToChannel
from utils import find_synonyms

if __name__ == "__main__":

    log_name = "wordsSynonyms"
    exchange = 'words'
    host = 'rabbitmq'
    queue = 'words.synonyms'
    mode = find_synonyms

    ConnectToChannel(log_name, exchange, host, queue, mode)
