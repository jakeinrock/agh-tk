import sys
import os
import pika
import json

dir = os.path.dirname(os.getcwd())
sys.path.insert(1, dir)

from PythonServicesConfig.main import ConnectToChannel


class ConnectExtractorToChannel(ConnectToChannel):
    """Customized connection to the channel"""
    def __init__(self, log_name, exchange, host, queue, mode, routing_key):
        self.routing_key = routing_key

        super().__init__(log_name, exchange, host, queue, mode)


    def publish(self, message, routing_key, exchange):
        """Publishing the message"""
        self._channel.basic_publish(exchange,
                                    routing_key,
                                    body=json.dumps(message),
                                    properties=pika.BasicProperties(
                                        content_encoding='utf-8')
                                    )

    def callback(self, ch, method, properties, body):
        """Customizng a callback"""
        message = json.loads(body)
        myfile = message['file']

        self.logger.info(f'Received file: {myfile}')

        try:
            extracted = self.extract(myfile)
            message["text"] = extracted
            message['fileState']['fileProcessed'] = True
            message['fileState']['fileProcessingError'] = False
            self.publish(message, routing_key='result', exchange='result')
            self.logger.info(f'Message was successfully forwarded with routing key: result')
        except Exception as e:
            message['fileState']['fileProcessed'] = False
            message['fileState']['fileProcessingError'] = True
            self.logger.warning(f'An error occurred while sending with routing key: result. Error - {e}')
        finally:
            self.publish(message, self.routing_key, self.exchange)
            self.logger.info(f'Message was successfully forwarded with routing key: {self.routing_key}')
            self.logger.info(f'Published Message: {message}')

    def extract(self, file):
        file = os.path.join(file)
        with open(file, 'r') as f:
            msg = f.read()
        return msg
