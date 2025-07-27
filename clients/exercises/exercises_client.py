from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient
from clients.private_http_builder import (
    get_private_http_client, AuthenticationUserDict
)


class Exercise(TypedDict):
    """
    Описание структуры упражнения.
    """
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class GetExercisesQueryDict(TypedDict):
    """
    Описание структуры запроса на получение упражнений
    """
    courseId: str


class CreateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса на создание упражнения
    """
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class GetExercisesResponseDict(TypedDict):
    """
    Описание структуры ответа получения упражнениц.
    """
    exercises: list[Exercise]


class UpdateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса на обновление упражнения
    """
    title: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class GetExerciseResponseDict(TypedDict):
    """
    Описание структуры запроса на получение упражнения.
    """
    exercise: Exercise


class CreateExerciseResponseDict(TypedDict):
    """
    Описание структуры запроса создание упражнения.
    """
    exercise: Exercise


class UpdateExerciseResponseDict(TypedDict):
    """
    Описание структуры запроса обновления упражнения.
    """
    exercise: Exercise


class ExercisesClient(APIClient):
    """
    Класс для работы с /api/v1/exercises
    """

    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        """
        Метод получает все упражнения по идентификатору курса.

        :param query: Словарь с courseId
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(url="/api/v1/exercises", params=query)

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения упражнения по его идентификатору.

        :param exercise_id: Идентификатор упражнения
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(url=f"/api/v1/exercise/{exercise_id}")

    def create_exercise_api(self, request: CreateExerciseRequestDict) -> Response:
        """
        Метод создания упражнения.

        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex,
        description и estimatedTime
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(url="/api/v1/exercises", json=request)

    def update_exercise_api(
            self,
            exercise_id: str,
            request: UpdateExerciseRequestDict
    ) -> Response:
        """
        Метод обновления упражнения.

        :param exercise_id: Идентификатор упражнения
        :param request: Словарь с title, maxScore, minScore, orderIndex,
        description и estimatedTime
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(url=f"/api/v1/exercises/{exercise_id}", json=request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления упражнения.

        :param exercise_id: Идентификатор упражнения
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(url=f"/api/v1/exercises/{exercise_id}")

    def get_exercises(self, query: GetExercisesQueryDict) -> GetExercisesResponseDict:
        response = self.get_exercises_api(query=query)
        return response.json()

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseDict:
        response = self.get_exercise_api(exercise_id=exercise_id)
        return response.json()

    def create_exercise(self, request: CreateExerciseRequestDict) -> CreateExerciseResponseDict:
        response = self.create_exercise_api(request=request)
        return response.json()

    def update_exercise(
            self,
            exercise_id: str,
            request: UpdateExerciseRequestDict
    ) -> UpdateExerciseResponseDict:
        response = self.update_exercise_api(exercise_id=exercise_id, request=request)
        return response.json()


def get_exercises_client(user: AuthenticationUserDict) -> ExercisesClient:
    """
    Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию ExercisesClient.
    """
    return ExercisesClient(client=get_private_http_client(user))
