from httpx import Response

from clients.api_client import APIClient
from clients.private_http_builder import (
    AuthenticationUserDict, get_private_http_client
)
from clients.courses.courses_schema import (
    GetCoursesQueryScheme, CreateCourseRequestScheme,
    UpdateCourseRequestScheme, CreateCourseResponseScheme
)


class CoursesClient(APIClient):
    """
    Клиент для работы с /api/v1/courses
    """

    def get_courses_api(self, query: GetCoursesQueryScheme) -> Response:
        """
        Метод получения списка курсов.

        :param query: Словарь с userId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(url="/api/v1/courses", params=query.model_dump(by_alias=True))

    def get_course_api(self, course_id: str) -> Response:
        """
        Метод получения курса.

        :param course_id: Идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(url=f"/api/v1/courses/{course_id}")

    def create_course_api(self, request: CreateCourseRequestScheme) -> Response:
        """
        Метод создания курса.

        :param request: Словарь с title, maxScore, minScore, description, estimatedTime,
        previewFileId, createdByUserId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(url="/api/v1/courses", json=request.model_dump(by_alias=True))

    def update_course_api(self, course_id: str, request: UpdateCourseRequestScheme) -> Response:
        """
        Метод обновления курса.

        :param course_id: Идентификатор курса.
        :param request: Словарь с title, maxScore, minScore, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(url=f"/api/v1/courses/{course_id}", json=request.model_dump(by_alias=True))

    def delete_course_api(self, course_id: str) -> Response:
        """
        Метод удаления курса.

        :param course_id: Идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(url=f"/api/v1/courses/{course_id}")

    def create_course(self, request: CreateCourseRequestScheme) -> CreateCourseResponseScheme:
        response = self.create_course_api(request=request)
        return CreateCourseResponseScheme.model_validate_json(response.text)


def get_courses_client(user: AuthenticationUserDict) -> CoursesClient:
    """
    Функция создаёт экземпляр CoursesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию CoursesClient.
    """
    return CoursesClient(client=get_private_http_client(user))
