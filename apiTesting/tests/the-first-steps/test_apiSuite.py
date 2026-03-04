import requests
import pytest
from base64 import b64encode
from jsonschema import validate

swagger = "https://petstore.swagger.io/v2/"
rabbit = {
    "name": "Jasper",
    "photoUrls": [
        "https://img.freepik.com/free-photo/furry-cute-rabbit-isolated_78492-3950.jpg",
    ],
}
postman_echo = "https://postman-echo.com/"
http_bin = "https://httpbin.org"

postman = {
    "name": rabbit["name"],
    "email": "test@example.com",
    "password": "password",
}

source_nasa = "https://api.nasa.gov/"
nasa_key = "xkQWv4DmUYsNdCh52vwFYhnfVhuJfZdkEKgFhrl3"

auth_token = {
    "Authorization": "Basic cG9zdG1hbjpwYXNzd29yZA=="
}

credential = b64encode(b"postman:password").decode()
auth_token_basic64 = {
    "Authorization": f"Basic {credential}"
}



def test_get_request_with_auth_header_token():
    response = requests.get(postman_echo + "basic-auth", headers=auth_token)
    assert response.status_code == 200
    assert response.json()["authenticated"] is True


def test_get_request_with_basic_64_auth():
    response = requests.get(postman_echo + "basic-auth", headers=auth_token_basic64)
    assert response.status_code == 200
    assert response.json()["authenticated"] is True
    assert response.request.headers["Authorization"] == auth_token_basic64["Authorization"]


def test_post_request_verify_create_pet():
    response = requests.post(swagger + "pet", json=rabbit)
    if response.status_code == 200:
        assert response.json()["name"] == rabbit["name"]
    else:
        assert response.status_code == 403


def test_post_request_verify_creating_user_with_form_data():
    response = requests.post(postman_echo + "post", data=postman)
    assert response.status_code == 200
    for key in postman:
        assert response.json()["form"][key] == postman[key]


def test_post_request_with_file_upload():
    files = {
        "attachment": open("static/Bear.jpg", "rb")
    }
    response = requests.post(http_bin + "/post", data=postman, files=files)
    assert response.status_code == 200
    assert "attachment" in response.json()["files"]


def test_set_cookie_and_redirect():
    cookies = {"name": "theHighTower", "value": "theRedBird"}
    response = requests.get(
        f"{http_bin}/cookies/set?{cookies['name']}={cookies['value']}",
        allow_redirects=False,
    )
    assert response.status_code == 302
    assert response.headers["Location"] == "/cookies"
    assert f"{cookies['name']}={cookies['value']}" in response.headers["Set-Cookie"]


def test_if_modified_since_or_none_match():
    headers = {
        "If-Modified-Since": "friday, 31 december 2000",
        "If-None-Match": "778855",
    }
    response = requests.get(http_bin + "/cache", headers=headers)

    if headers.get("If-Modified-Since") or headers.get("If-None-Match"):
        assert response.status_code == 304
    else:
        assert response.status_code == 200

@pytest.mark.skip(reason="It works if there are additional tools for accessing the resource")
def test_validate_json_response_with_schema():
    schema = {
        "type": "object",
        "properties": {
            "date": {"type": "string"},
            "title": {"type": "string"},
            "explanation": {"type": "string"},
            "media_type": {"type": "string"},
            "url": {"type": "string"},
        },
        "required": ["date", "title"],
        "additionalProperties": True,
    }

    response = requests.get(
        f"{source_nasa}planetary/apod?api_key={nasa_key}"
    )

    validate(instance=response.json(), schema=schema)
    assert response.status_code in [200, 403]