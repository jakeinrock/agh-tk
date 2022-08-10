import unittest
from create_connect import ConnectAudioExtractorToChannel
import logging

class TestSum(unittest.TestCase):

    def test_eng(self):
        res = ConnectAudioExtractorToChannel.extract('audio_samples/sample_eng.wav', logging.getLogger("test-logger"))
        self.assertIn('high', res)

    def test_pl(self):
        res = ConnectAudioExtractorToChannel.extract('audio_samples/sample_pl.wav', logging.getLogger("test-logger"))
        self.assertIn('jest', res)

if __name__ == '__main__':
    unittest.main()
