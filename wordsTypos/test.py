import pytest

from utils import create_typos

@pytest.fixture
def run_test():
    test_class = create_typos(words=['kot'])
    result = test_class.find_form()

    return result

def test(run_test):

    expected = ['jot', 'kit', 'kor']
    assert run_test == expected
