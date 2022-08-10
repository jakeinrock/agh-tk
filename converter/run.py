from create_connect import ConnectConverterToChannel

if __name__ == "__main__":

    ConnectConverterToChannel(
        log_name="converter",
        exchange="words",
        host="rabbitmq",
        queue="format.unconverted",
        routing_key="words.scraper",
        )
