from create_connect import ConnectConverterToChannel

if __name__ == "__main__":


    log_name = "converter"
    exchange = "words"
    host = "rabbitmq"
    queue = "format.unconverted"
    mode = None
    routing_key = "words.scraper"

    ConnectConverterToChannel(log_name, exchange, host, queue, mode, routing_key)