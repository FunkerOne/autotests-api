from pydantic import BaseModel, Field, ConfigDict


class ExerciseScheme(BaseModel):
    """
    Описание структуры упражнения.
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")


class GetExercisesQueryScheme(BaseModel):
    """
    Описание структуры запроса на получение упражнений.
    """
    model_config = ConfigDict(populate_by_name=True)

    course_id: str = Field(alias="courseId")


class CreateExerciseRequestScheme(BaseModel):
    """
    Описание структуры запроса на создание упражнения.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")


class GetExercisesResponseSchema(BaseModel):
    """
    Описание структуры ответа получения упражнениц.
    """
    exercises: list[ExerciseScheme]


class UpdateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление упражнения.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")


class GetExerciseResponseSchema(BaseModel):
    """
    Описание структуры запроса на получение упражнения.
    """
    exercise: ExerciseScheme
    

class CreateExerciseResponseSchema(BaseModel):
    """
    Описание структуры запроса создание упражнения.
    """
    exercise: ExerciseScheme


class UpdateExerciseResponseSchema(BaseModel):
    """
    Описание структуры запроса обновления упражнения.
    """
    exercise: ExerciseScheme
