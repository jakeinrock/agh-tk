from create_connect import ConnectAudioExtractorToChannel

if __name__ == "__main__":

    ConnectAudioExtractorToChannel(
        log_name="audio_service",
        exchange="text",
        host="rabbitmq",
        queue="format.audio",
        routing_key="text",
    )
