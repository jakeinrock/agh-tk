from create_connect import ConnectExtractorToChannel

if __name__ == "__main__":

    ConnectExtractorToChannel(
        log_name="textExtractor",
        exchange="text",
        host='rabbitmq',
        queue='format.txt',
        routing_key="text",
        )
