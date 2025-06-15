from fastapi import status

from routers.todos import get_db, get_current_user
from main import app
from models import Todos
from .utils import *

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user


def test_read_all_authenticated(test_todo):
    response = client.get("/todos")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [{'completed':False, 'description':'desc', 'id':1, 'owner_id':1, 'title':"task1", 'priority':5,}]

def test_read_one_authenticated(test_todo):
    response = client.get("/todos/todo/1")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {'completed':False, 'description':'desc', 'id':1, 'owner_id':1, 'title':"task1", 'priority':5,}

def test_one_authenticated_not_found():
    response = client.get("/todos/todo/99")
    assert response.status_code == 404
    assert response.json() == {'detail': 'Todo not found'}

def test_create_todo(test_todo):
    request_data = {
        'title': 'New todo',
        'description': 'Desc',
        'priority': 5,
        'completed': False,
    }

    response = client.post('/todos/todo', json=request_data)
    assert response.status_code==201

    db = TestingSessionLocal()
    model = db.query(Todos).order_by(Todos.id.desc()).first()
    assert model.title == request_data.get('title')
    assert model.description == request_data.get('description')
    assert model.priority == request_data.get('priority')
    assert model.completed == request_data.get('completed')

def test_update_todo(test_todo):
    request_data = {
        'title': 'task1',
        'description': 'New Desc',
        'priority': 5,
        'completed': False,
    }

    response = client.put('/todos/todo/1', json=request_data)
    assert response.status_code==204

    db = TestingSessionLocal()
    model = db.query(Todos).filter(Todos.id == 1).first()
    assert model.description == 'New Desc'

def test_update_todo_not_found(test_todo):
    request_data = {
        'title': 'task1',
        'description': 'New Desc',
        'priority': 5,
        'completed': False,
    }

    response = client.put('/todos/todo/999', json=request_data)
    assert response.status_code == 404
    assert response.json() == {'detail': 'Not Found'}

def test_delete_todo(test_todo):
    response = client.delete('/todos/todo/1')
    assert response.status_code == 204

    db = TestingSessionLocal()
    model = db.query(Todos).filter(Todos.id == 1).first()
    assert model is None
    db.close()

def test_delete_todo_not_found(test_todo):
    response = client.delete('/todos/todo/999')
    assert response.status_code == 404
    assert response.json() == {'detail': 'Not Found'}


