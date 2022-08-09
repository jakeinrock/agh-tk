from create_connect import ConnectExtractorToChannel

if __name__ == "__main__":

    log_name = "textExtractor"
    exchange = "text"
    host = 'rabbitmq'
    queue = 'format.txt'
    mode = None
    routing_key = "text"

    ConnectExtractorToChannel(log_name, exchange, host, queue, mode, routing_key)
