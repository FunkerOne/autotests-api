import httpx

_BASE_URL = "http://localhost:8000/api/v1"
_AUTH_LOGIN = "/authentication/login"
_USER_ME = "/users/me"


def auth_login(email: str, password: str) -> dict:
    request = {
        "email": email,
        "password": password
    }
    return request


request = auth_login(email="user@example.com", password="password")
response = httpx.post(
    url=f"{_BASE_URL}{_AUTH_LOGIN}", json=request
).json().get("token", {})

access_token = response.get("accessToken", "")

headers = {"Authorization": f"Bearer {access_token}"}

try:
    response = httpx.get(
        url=f"{_BASE_URL}{_USER_ME}", headers=headers
    )
    response.raise_for_status()
except httpx.HTTPStatusError as e:
    print(f"Ошибка: {e}")

print(response.status_code)
print(response.json())
