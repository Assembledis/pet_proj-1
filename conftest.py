import pytest
import faker
from api_clients import APIClient
from config import BASE_URL

fake = faker.Faker()

@pytest.fixture
def client():
    return APIClient(BASE_URL)
@pytest.fixture
def generate_post_data():
    def _generate():
        return {
            "title": fake.sentence(nb_words=3),
            "body": fake.paragraph(nb_sentences=2),
            "userId": fake.random_int(min=1, max=10)
        }
    return _generate