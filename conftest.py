import pytest
import helpers.user_helpers as user_helpers
import random

@pytest.fixture()
def create_test_user():
    random_number = random.randint(1000, 9999)
    email = f"test{random_number}@example.com"
    password = "testpassword"
    name = f"Test User {random_number}"

    response = user_helpers.create_user(email, password, name)
    assert response.status_code == 200

    login_response = user_helpers.login_user(email, password)
    token = login_response.json().get("accessToken")
    
    yield {
        "email": email,
        "password": password,
        "name": name,
        "token": token  
    }
    user_helpers.delete_user(token)