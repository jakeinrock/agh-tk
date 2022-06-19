import unittest
from converter_callback import ConverterCallback
import logging
import os

class TestSum(unittest.TestCase):

    def test_eng(self):
        ConverterCallback.convert('samples/eng.mp3', logging.getLogger("test-logger"), path=os.getcwd())
        self.assertTrue(os.path.exists(".mp3-converted/eng.wav"))

    def test_pl(self):
        ConverterCallback.convert('samples/pl_text_eng_audio.mp4', logging.getLogger("test-logger"), path=os.getcwd())
        self.assertTrue(os.path.exists(".mp4-converted/pl_text_eng_audio.wav"))

if __name__ == '__main__':
    unittest.main()