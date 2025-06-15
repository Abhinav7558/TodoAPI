from .utils import *
from routers.users import get_db, get_current_user

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user


def test_get_user(test_user):
    response = client.get("/users/get_user")
    assert response.status_code == 200
    assert response.json()['username'] == "user1"
    assert response.json()['email'] == "user@example.com"
    assert response.json()['first_name'] == "user"
    assert response.json()['last_name'] == "1"
    assert response.json()['role'] == "admin"
    assert response.json()['phone_number'] == "1234567890"

def test_change_password_success(test_user):
    response = client.put('/users/change_password', json={'password': 'password', 'new_password': 'newpassword'})
    assert response.status_code == 201

def test_change_password_unsuccessful(test_user):
    response = client.put('/users/change_password', json={'password': 'wrongpassword', 'new_password': 'newpassword'})
    assert response.status_code == 401
    assert response.json() == {'detail':'Error on password change'}

def test_change_phone_no_success(test_user):
    response = client.put('/users/phone_number/1482937291')
    assert response.status_code == 201
