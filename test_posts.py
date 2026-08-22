from jsonschema import validate
from api_clients import APIClient
from config import BASE_URL
from schemas import POST_SCHEMA
import allure_pytest
import allure

client = APIClient(BASE_URL)

def test_valid_post():
    payload = {"title": "foo", "body": "bar", "userId": 1}
    response = client.post("/posts", json=payload)
    assert response.status_code == 201
    validate(instance=response.json(), schema=POST_SCHEMA)
def test_invalid_post():
    payload = {"title": "132", "body": "bar", "userId": 111111111111111111111111}
    response = client.post("/posts/1213213231122132132", json=payload)
    assert response.status_code == 404
    assert response.json() == {}
def test_valid_get_post():
    response = client.get("/posts/1")
    assert response.status_code == 200
    validate(instance=response.json(), schema=POST_SCHEMA)
def test_invalid_get_post():
    response = client.get("/posts/141222222222222222")
    assert response.status_code == 404
    assert response.json() == {}
def test_patch_post():
    payload = {"title": "foo", "body": "bar"}
    response = client.patch("/posts/1", json=payload)
    assert response.status_code == 200
    validate(instance=response.json(), schema=POST_SCHEMA)


def test_valid_posts(client, generate_post_data):
    payload = generate_post_data()

    response = client.post("/posts", json=payload)
    assert response.status_code == 201

    data = response.json()
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
@allure.feature("Posts API")
@allure.story("Create Post")
def test_valid_posts(client, generate_post_data):
  with allure.step("Генерация тестовых данных"):
    payload = generate_post_data()

  with allure.step("Отправка POST-запроса на создание поста"):
    response = client.post("/posts", json=payload)

  with allure.step("Проверка статуса ответа"):
    assert response.status_code == 201

  with allure.step("Проверка тела ответа"):
    data = response.json()
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
