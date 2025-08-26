import pytest

from http import HTTPStatus

from clients.exercises.exercises_client import ExercisesClient
from clients.exercises.exercises_schema import (
    CreateExerciseRequestSchema, CreateExerciseResponseSchema
)
from fixtures.courses import CourseFixture
from tools.assertions.base import assert_status_code
from tools.assertions.exercises import assert_create_exercise_response
from tools.assertions.schema import validate_json_schema


@pytest.mark.exercises
@pytest.mark.regression
class TestExercises:
    def test_create_exercises(
            self,
            exercises_client: ExercisesClient,
            function_course: CourseFixture
    ):
        request = CreateExerciseRequestSchema(
            course_id=function_course.response.course.id
        )
        response = exercises_client.create_exercise_api(request=request)
        response_date = CreateExerciseResponseSchema.model_validate_json(response.text)

        assert_status_code(actual=response.status_code, expected=HTTPStatus.OK)
        assert_create_exercise_response(request=request, response=response_date)

        validate_json_schema(instance=response.json(), schema=response_date.model_json_schema())
