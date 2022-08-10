import time
import pika
import json

import pika.exceptions

from .utils import create_logger

class ConnectToChannel:
    """Connecting to the channel with received parameters."""
    def __init__(self, log_name, exchange, host, queue, **kwargs):

        self.exchange = exchange
        self.host = host
        self.queue = queue
        if 'mode' in kwargs:
            self.mode = kwargs['mode']
        if 'routing_key' in kwargs:
            self.routing_key = kwargs['routing_key']
        self.logger = create_logger(log_name)

        flag = 0
        while flag == 0:
            try:
                time.sleep(5.0)
                self._connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.host))
                self._channel = self._connection.channel()

                self.logger.info('Connected to channel')
                flag = 1
            except pika.exceptions.AMQPConnectionError:
                self.logger.warning('Cannot connect to channel - retrying in 10 seconds...')
                time.sleep(5.0)

        self._startserver()

    def _startserver(self):
        """Starting the server"""
        self._channel.basic_consume(
            queue=self.queue,
            on_message_callback=self.callback,
            auto_ack=True)

        self._channel.start_consuming()
        self.logger.info('Server started waiting for Messages')

    def publish(self, message, routing_key, **kwargs):
        if 'exchange' not in kwargs:
            exchange = self.exchange
        else:
            exchange = kwargs['exchange']
        """Publishing the message"""
        self._channel.basic_publish(exchange=exchange,
                                    routing_key=routing_key,
                                    body=json.dumps(message),
                                    properties=pika.BasicProperties(
                                        content_encoding='utf-8')
                                    )

    def callback(self, ch, method, properties, body):
        """Customizng a callback"""
        message = json.loads(body)
        my_words = message['phrase'].split()

        self.logger.info(f'Message received: {message}')
        self.logger.info(f'Words received: {my_words}')

        results = self.mode(my_words)
        for res in results:
            if res not in message['words']:
                message['words'].append(res)

        queueKey = message["filters"]["searchModes"][0]
        message["filters"]["searchModes"].pop(0)
        message["filters"]["searchModes"].append(queueKey)

        new_search_mode = "words." + message["filters"]["searchModes"][0]

        self.publish(message, new_search_mode)

        self.logger.info(f'The Message was forwarded to: {new_search_mode}')
        self.logger.info(f'Published Message: {message}')
