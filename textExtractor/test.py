import pytest
import os


@pytest.fixture
def run_test():
    result = extract(file='test.txt')
    return result

def extract(self, file):
    file = os.path.join(file)
    with open(file, 'r') as f:
        msg = f.read()
    return msg

def test(run_test):

    expected = 'Testing text extractor.\nLine 1\nLine 2'
    assert run_test == expected
