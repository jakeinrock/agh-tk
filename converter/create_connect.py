import sys
import os
import pika
import json
import subprocess

dir = os.path.dirname(os.getcwd())
sys.path.insert(1, dir)

from PythonServicesConfig.main import ConnectToChannel


class ConnectConverterToChannel(ConnectToChannel):
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
        myfile = message["file"]
        self.logger.info(f"Received file: {myfile}")

        try:
            converter_file_path = self.convert(myfile)
            message["audio"] = {}
            message["audio"]["filePathInVolume"] = converter_file_path
            message["fileState"]["fileProcessed"] = True
            message["fileState"]["fileProcessingError"] = False
            self.publish(message, self.host, routing_key="result", exchange="result")
            self.logger.info("Message was successfully forwarded with routing key: result")
        except Exception as e:
            message['fileState']['fileProcessed'] = False
            message['fileState']['fileProcessingError'] = True
            self.logger.warning(f'An error occurred while converting or sending with routing key: result, err: {e}')
        finally:
            self.publish(message, self.host, self.routing_key, self.exchange)
            self.logger.info(f'Message was successfully forwarded with routing key: {self.routing_key}')
            self.logger.info(f'Published Message: {message}')

    def convert(self, file, logger, path='/host/extracted') -> str:
        filename = os.path.basename(file)
        name, ext = os.path.splitext(filename)

        output_dir = os.path.join(path, f"{ext}-converted")
        if not os.path.isdir(output_dir):
            os.makedirs(output_dir, exist_ok=True)

        dst = os.path.abspath(os.path.join(output_dir, f"{name}.wav"))

        if os.path.exists(dst):
            self.logger.info(f"{dst} file already exists, returning it")
            return dst

        self.logger.info(f"Dst file = {dst}")

        if ext == ".mp3":
            subprocess.call(f"ffmpeg -i {file} {dst}", shell=True)
        elif ext == ".mp4":
            subprocess.call(f"ffmpeg -i {file} -ab 160k -ac 2 -ar 44100 -vn {dst}", shell=True)
        else:
            raise Exception(f"Unsupported conversion extension {ext}")

        return dst
