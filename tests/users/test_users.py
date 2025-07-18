import pytest

# from configuration import SERVICE_URL
from src.baseclasses.Response import Response
from src.schemas.user import User
from src.schemas.computer import Computer
from example import computer


def test_getting_users_list(get_users, make_number):
    Response(get_users).assert_status_code(200).validate(User)
    # print(get_number)
    # print(calculate)
    # print(calculate(1, 1))
    # print(make_number)


@pytest.mark.development
@pytest.mark.production
@pytest.mark.skip('[ISSUE-111] Issue with network connection')
def test_another():
    """
    In that test we try to check that  is equal to 2
    """
    assert 1 == 1


@pytest.mark.development
@pytest.mark.parametrize('first_value, second_value, result', [
    (1, 2, 3),
    (-1, -2, -3),
    (-1, 2, 1),
    ('b', -2, None),
    ('b', 'b', None),
])
def test_calculator(first_value, second_value, result, calculate):
    """
    In test we are testing calculating with different values (valid and invalid).
    """
    assert calculate(first_value, second_value) == result


@pytest.mark.development
@pytest.mark.production
def test_another_failing_test():
    assert 1 == 2


def test_pydantic_object():
    comp = Computer.model_validate(computer)
    print(comp.detailed_info.physical.color.as_hex())
