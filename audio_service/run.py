from create_connect import ConnectAudioExtractorToChannel

if __name__ == "__main__":

    log_name = "audio_service"
    exchange = "text"
    host = "rabbitmq"
    queue = "format.audio"
    mode = None
    routing_key = "text"

    ConnectAudioExtractorToChannel(log_name, exchange, host, queue, mode, routing_key)
    