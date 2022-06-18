import unittest
from audio_extractor_callback import AudioExtractorCallback
import logging

class TestSum(unittest.TestCase):

    def test_eng(self):
        res = AudioExtractorCallback.extract('audio_samples/sample_eng.wav', logging.getLogger("test-logger"))
        self.assertIn('high', res)

    def test_pl(self):
        res = AudioExtractorCallback.extract('audio_samples/sample_pl.wav', logging.getLogger("test-logger"))
        self.assertIn('jest', res)

if __name__ == '__main__':
    unittest.main()