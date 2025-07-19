import time

import httpx

_BASE_URL = "http://localhost:8000/api/v1"


def get_random_email() -> str:
    return f"test.{time.time()}@example.com"


create_user_payload = {
    "email": get_random_email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}
create_user_response = httpx.post(url=f"{_BASE_URL}/users", json=create_user_payload)
create_user_response_data = create_user_response.json()
print('Create user data:', create_user_response_data)


login_payload = {
    "email": create_user_payload.get("email"),
    "password": create_user_payload.get("password")
}
login_response = httpx.post(url=f"{_BASE_URL}/authentication/login", json=login_payload)
login_response_data = login_response.json()
print('Login data:', login_response_data)


get_user_headers = {
    "Authorization": f"Bearer {login_response_data.get("token")["accessToken"]}"
}
update_user_payload = {
    "email": get_random_email(),
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}
get_user_id = create_user_response_data.get("user")["id"]
update_user_response = httpx.patch(
    url=f"{_BASE_URL}/users/{get_user_id}",
    json=update_user_payload,
    headers=get_user_headers
)
update_user_response_data = update_user_response.json()
print("Update user data:", update_user_response_data)
