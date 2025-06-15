from .utils import *
from routers.admin import get_db, get_current_user
from models import Todos

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user


def test_admin_read_all_authenticated(test_todo):
    response = client.get('/admin/todo')
    assert response.status_code == 200
    assert response.json() == [{'completed':False, 'description':'desc', 'id':1, 'owner_id':1, 'title':"task1", 'priority':5, 'owner_id':1}]

def test_admin_delete_todo(test_todo):
    response = client.delete('/admin/todo/1')
    assert response.status_code == 204

    db = TestingSessionLocal()
    model = db.query(Todos).filter(Todos.id == 1).first()
    assert model is None
    db.close()

def test_admin_delete_todo_not_found(test_todo):
    response = client.delete('/admin/todo/999')
    assert response.status_code == 404
    assert response.json() == {'detail': 'Not Found'}