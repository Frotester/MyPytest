import pytest
from src.generators.player_localization import PlayerLocalization
import requests
from configuration import SERVICE_URL
from src.baseclasses.Response import Response
from src.schemas.user import User
import tables

from src.enums.user_enums import Statuses


def test_equal():
    assert 1 == 1, "Number is not equal expected"


def test_is_not_equal():
    assert 1 != 2, "Number is equal"


def test_getting_posts():
    response = requests.get(url=SERVICE_URL)
    response = Response(response)
    response.assert_status_code(200).validate(User)


@pytest.mark.parametrize('status', Statuses.list())
def test_generator_changing(status, get_player_generator):
    print(get_player_generator.set_status(status).build())


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
def test_deleting_keys_in_object(delete_key, get_player_generator):
    object_to_send = get_player_generator.build()
    del object_to_send[delete_key]
    print(object_to_send)


@pytest.mark.parametrize("localizations, loc", [
    ("fr", "fr_FR")
])
def test_updating_localization_in_generator(get_player_generator,
                                            localizations,
                                            loc):
    object_to_send = get_player_generator.update_inner_value(
        ['localize', localizations],
        PlayerLocalization(loc).set_number(10).build()
    ).build()
    print(object_to_send)


def test_get_data_users(get_db_session):
    data = get_db_session.query(tables.Users).first()
    print(data.age)


def test_try_to_delete_something(get_delete_method, get_db_session):
    get_delete_method(get_db_session, tables.Users, (tables.Users.id == 1))


def test_try_to_add_testdata(get_db_session, get_add_method):
    new_item = {'username': 'Tihon', 'email': 'Tihon@mail.ru', 'age': 15}
    item = tables.Users(**new_item)
    get_add_method(get_db_session, item)
    print(item)


def test_try_to_add_testdata(
        get_db_session, get_add_method, get_item_type_generator
):

    item = tables.ItemType(**get_item_type_generator.build())
    get_add_method(get_db_session, item)
    print(item.item_id)


def test_try_to_add_testdata2(generate_item_type):
    print(generate_item_type.item_id)
