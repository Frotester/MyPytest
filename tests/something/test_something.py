import requests
from configuration import SERVICE_URL
from src.baseclasses.Response import Response
# from src.json_schemas.post import POST_SCHEMA
from src.pydantic_schemas.post import Post

# def test_equal():
#     assert 1 == 1, "Number is not equal expected"
#
# def test_is_not_equal():
#     assert 1 != 2, "Number is equal"


# def test_getting_posts():
#     response = requests.get(url=SERVICE_URL)
#     response = Response(response)
#
#     response.assert_status_code(200).validate(Post)


def test_something(get_number):
    assert 1 == 1
    print(get_number)