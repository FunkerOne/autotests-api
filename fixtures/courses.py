import pytest

from clients.courses.courses_client import (
    CoursesClient, get_courses_client
)
from clients.courses.courses_schema import (
    CreateCourseRequestScheme, CreateCourseResponseScheme
)
from fixtures.files import FileFixture
from fixtures.users import UserFixture
from pydantic import BaseModel


class CourseFixture(BaseModel):
    request: CreateCourseRequestScheme
    response: CreateCourseResponseScheme


@pytest.fixture
def courses_client(function_user: UserFixture) -> CoursesClient:
    return get_courses_client(user=function_user.authentication_user)


@pytest.fixture
def function_course(
        courses_client: CoursesClient,
        function_user: UserFixture,
        function_file: FileFixture
) -> CourseFixture:
    request = CreateCourseRequestScheme()
    response = courses_client.create_course(request=request)
    return CourseFixture(request=request, response=response)
