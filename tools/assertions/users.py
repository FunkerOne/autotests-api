from clients.users.users_schema import (
    CreateUserRequestSchema, CreateUserResponseSchema, UserSchema
)
from tools.assertions.base import assert_equal


def assert_create_user_response(request: CreateUserRequestSchema, response: CreateUserResponseSchema):
    """
    Проверяет, что ответ на создание пользователя соответствует запросу.

    :param request: Исходный запрос на создание пользователя.
    :param response: Ответ API с данными пользователя.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(response.user.email, request.email, "email")
    assert_equal(response.user.last_name, request.last_name, "last_name")
    assert_equal(response.user.first_name, request.first_name, "first_name")
    assert_equal(response.user.middle_name, request.middle_name, "middle_name")


def assert_user(actual: UserSchema, expect: UserSchema):
    assert_equal(actual.user.id, expect.user.id, "id")
    assert_equal(actual.user.email, expect.user.email, "email")
    assert_equal(actual.user.last_name, expect.user.last_name, "last_name")
    assert_equal(actual.user.first_name, expect.user.first_name, "first_name")
    assert_equal(actual.user.middle_name, expect.user.middle_name, "middle_name")


def assert_get_user_response(actual, expect):
    assert_user(actual, expect)
