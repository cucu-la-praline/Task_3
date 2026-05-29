import requests
from faker import Faker

fake = Faker()


def generate_user_data():
    return {
        "email": fake.email(),
        "password": fake.password(length=10),
        "name": fake.first_name()
    }


def create_user_via_api(base_url):
    """Создание пользователя через API"""
    user_data = generate_user_data()
    response = requests.post(f"{base_url}/api/auth/register", json=user_data)

    if response.status_code == 200:
        token = response.json().get("accessToken", "")
        return user_data, token
    return user_data, None


def delete_user_via_api(base_url, token):
    """Удаление пользователя через API"""
    if token:
        headers = {"Authorization": token}
        requests.delete(f"{base_url}/api/auth/user", headers=headers)