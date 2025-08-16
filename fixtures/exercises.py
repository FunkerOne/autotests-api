import pytest

from clients.exercises.exercises_client import (
    ExercisesClient, get_exercises_client
)
from clients.exercises.exercises_schema import (
    CreateExerciseRequestScheme, CreateExerciseResponseSchema
)
from fixtures.courses import CourseFixture
from fixtures.users import UserFixture
from pydantic import BaseModel


class ExerciseFixture(BaseModel):
    request: CreateExerciseRequestScheme
    response: CreateExerciseResponseSchema


@pytest.fixture
def exercises_client(function_user: UserFixture) -> ExercisesClient:
    return get_exercises_client(user=function_user.authentication_user)


@pytest.fixture
def function_exercise(
        exercises_client: ExercisesClient,
        function_course: CourseFixture
) -> ExerciseFixture:
    request = CreateExerciseRequestScheme()
    response = exercises_client.create_exercise(request=request)
    return ExerciseFixture(request=request, response=response)
