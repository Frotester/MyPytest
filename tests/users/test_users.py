import requests

from configuration import SERVICE_URL
from src.baseclasses.Response import Response
from src.schemas.user import User


def test_getting_users_list(get_users, get_number):
    Response(get_users).assert_status_code(200).validate(User)
    print(get_number)


def test_another():
    assert 1 == 1
