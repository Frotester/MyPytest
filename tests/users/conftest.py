import pytest
import requests

from configuration import SERVICE_URL

# @pytest.ini.fixture(scope='function')
# def say_hello():
#     print("Hello")
#     return 14

@pytest.fixture
def get_users():
    resp = requests.get(SERVICE_URL)
    return resp

