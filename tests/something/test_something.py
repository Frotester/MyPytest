import pytest
from src.generators.player_localization import PlayerLocalization
import requests
from configuration import SERVICE_URL
from src.baseclasses.Response import Response
# from src.json_schemas.post import POST_SCHEMA
from src.schemas.user import User
from src.pydantic_schemas.post import Post

from src.enums.user_enums import Statuses


def test_equal():
    assert 1 == 1, "Number is not equal expected"


def test_is_not_equal():
    assert 1 != 2, "Number is equal"


def test_getting_posts():
    response = requests.get(url=SERVICE_URL)
    response = Response(response)

    response.assert_status_code(200).validate(User)


@pytest.mark.parametrize('status', [
    *Statuses.list()
])
def test_something(status, get_player_generator):
    print(get_player_generator.build())


@pytest.mark.parametrize('status', [
     'ACTIVE',
     'BANNED',
     'DELETED',
     'INACTIVE'
])
def test_something1(status, get_player_generator):
    print(get_player_generator.set_status(status).build())


@pytest.mark.parametrize('balance_value', [
    '100',
    '0',
    '-10',
    'ddd'
])
def test_something2(balance_value, get_player_generator):
    print(get_player_generator.set_balance(balance_value).build())


@pytest.mark.parametrize('delete_key', [
     'account_status',
     'balance',
     'localize',
     'avatar'
])
def test_something3(delete_key, get_player_generator):
    object_to_send = get_player_generator.build()
    del object_to_send[delete_key]
    print(object_to_send)


@pytest.mark.parametrize("localizations, loc", [
    ("fr", "fr_FR")
])
def test_something4(get_player_generator, localizations, loc):
    object_to_send = get_player_generator.update_inner_value(
        ['localize', localizations], PlayerLocalization(loc).set_number(10).build()
    ).build()
    print(object_to_send)