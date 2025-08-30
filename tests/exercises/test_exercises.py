import pytest

from http import HTTPStatus

from clients.errors_schema import InternalErrorResponseSchema
from clients.exercises.exercises_client import ExercisesClient
from clients.exercises.exercises_schema import (
    CreateExerciseRequestSchema, CreateExerciseResponseSchema,
    GetExerciseResponseSchema, UpdateExerciseRequestSchema,
    UpdateExerciseResponseSchema, GetExercisesQuerySchema,
    GetExercisesResponseSchema
)
from fixtures.courses import CourseFixture
from fixtures.exercises import ExerciseFixture
from tools.assertions.base import assert_status_code
from tools.assertions.exercises import (
    assert_create_exercise_response, assert_get_exercise_response,
    assert_update_exercise_response, assert_exercise_not_found_response,
    assert_get_exercises_response
)
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

    def test_get_exercise(
            self,
            exercises_client: ExercisesClient,
            function_exercise: ExerciseFixture
    ):
        exercise_id = function_exercise.response.exercise.id
        response = exercises_client.get_exercise_api(exercise_id=exercise_id)
        response_data = GetExerciseResponseSchema.model_validate_json(response.text)

        assert_status_code(actual=response.status_code, expected=HTTPStatus.OK)
        assert_get_exercise_response(
            get_exercise_response=response_data, create_exercise_response=function_exercise.response
        )

        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())

    def test_update_exercise(
            self,
            exercises_client: ExercisesClient,
            function_exercise: ExerciseFixture
    ):
        request = UpdateExerciseRequestSchema()
        response = exercises_client.update_exercise_api(
            exercise_id=function_exercise.response.exercise.id, request=request
        )
        response_data = UpdateExerciseResponseSchema.model_validate_json(response.text)

        assert_status_code(actual=response.status_code, expected=HTTPStatus.OK)
        assert_update_exercise_response(request=request, response=response_data)

        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())

    def test_delete_exercise(
            self,
            exercises_client: ExercisesClient,
            function_exercise: ExerciseFixture
    ):
        exercise_id = function_exercise.response.exercise.id
        response = exercises_client.delete_exercise_api(exercise_id=exercise_id)

        assert_status_code(actual=response.status_code, expected=HTTPStatus.OK)

        get_exercise_response = exercises_client.get_exercise_api(exercise_id=exercise_id)
        get_exercise_response_data = InternalErrorResponseSchema.model_validate_json(
            get_exercise_response.text
        )

        assert_status_code(
            actual=get_exercise_response.status_code, expected=HTTPStatus.NOT_FOUND
        )
        assert_exercise_not_found_response(actual=get_exercise_response_data)

        validate_json_schema(
            instance=get_exercise_response.json(),
            schema=get_exercise_response_data.model_json_schema()
        )

    def test_get_exercises(
            self,
            exercises_client: ExercisesClient,
            function_course: CourseFixture,
            function_exercise: ExerciseFixture
    ):
        query = GetExercisesQuerySchema(courseId=function_course.response.course.id)
        response = exercises_client.get_exercises_api(query=query)
        response_data = GetExercisesResponseSchema.model_validate_json(response.text)

        assert_status_code(actual=response.status_code, expected=HTTPStatus.OK)
        assert_get_exercises_response(
            get_exercises_response=response_data,
            create_exercise_responses=[function_exercise.response]
        )

        validate_json_schema(
            instance=response.json(),
            schema=response_data.model_json_schema()
        )
