import pytest
from pydantic import BaseModel

from clients.files.files_client import FilesClient, get_files_client
from clients.files.files_schema import CreateFileRequestSchem, CreateFileResponseSchema
from fixtures.users import UserFixture


class FileFixture(BaseModel):
    request: CreateFileRequestSchem
    response: CreateFileResponseSchema


@pytest.fixture
def files_client(function_user: UserFixture) -> FilesClient:
    return get_files_client(user=function_user.authentication_user)


@pytest.fixture
def function_file(files_client: UserFixture) -> FileFixture:
    request = CreateFileRequestSchem(upload_file="./testdata/files/image.png")
    response = files_client.create_file(request)
    return FileFixture(request=request, response=response)
