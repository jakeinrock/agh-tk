import sys
import os
import pika
import json
import speech_recognition as sr

dir = os.path.dirname(os.getcwd())
sys.path.insert(1, dir)

from PythonServicesConfig.main import ConnectToChannel


class ConnectAudioExtractorToChannel(ConnectToChannel):
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
            text_from_audio = self.extract(myfile)
            message["text"] = text_from_audio
            message["fileState"]["fileProcessed"] = True
            message["fileState"]["fileProcessingError"] = False
            self.publish(message, routing_key="result", exchange="result")
            self.logger.info("Message was successfully forwarded with routing key: result")
        except Exception as e:
            message['fileState']['fileProcessed'] = False
            message['fileState']['fileProcessingError'] = True
            self.logger.warning(f'An error occurred while extracting text from audio or sending with routing key result. Err = {e}')
        finally:
            self.publish(message, self.routing_key, self.exchange)
            self.logger.info(f'Message was successfully forwarded with routing key: {self.routing_key}')
            self.logger.info(f'Published Message: {message}')

    def extract(self, file) -> str:
        langs = ["en-US", "pl"]
        r = sr.Recognizer()
        file = os.path.join(file)

        text_in_all_langs = ""

        if not os.path.exists(file):
            raise Exception(f"Received file {file} doesn't exist")

        try:
            with sr.AudioFile(file) as source:
                r.adjust_for_ambient_noise(source, duration=0.5)
                audio = r.record(source)
                for lang in langs:
                    try:
                        text_in_all_langs = f"{text_in_all_langs}\n{r.recognize_google(audio, language=lang)}"
                    except sr.UnknownValueError:
                        self.logger.info(f"{file}: GSR could not understand audio")
                        raise Exception(f"{file}: Google Speech Recognition could not understand audio")
                    except sr.RequestError:
                        self.logger.info(f"{file}: Could not request results from GSR")
                        raise Exception(f"{file}: Could not request results from Google Speech Recognition service")
        except Exception:
            self.logger.info(f"{file}: Error while converting file to audio")
            raise Exception(f"{file}: Error while converting file to audio")

        return text_in_all_langs
