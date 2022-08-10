import sys
import os
import json

dir = os.path.dirname(os.getcwd())
sys.path.insert(1, dir)

from PythonServicesConfig.main import ConnectToChannel


class ConnectExtractorToChannel(ConnectToChannel):
    """Customized connection to the channel"""

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
            self.publish(message, routing_key=self.routing_key, exchange=self.exchange)
            self.logger.info(f'Message was successfully forwarded with routing key: {self.routing_key}')
            self.logger.info(f'Published Message: {message}')

    def extract(self, file):
        file = os.path.join(file)
        with open(file, 'r') as f:
            msg = f.read()
        return msg
