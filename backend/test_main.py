from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_get_all_users():
    response = client.get("/users")
    assert response.status_code == 200
    assert "users" in response.json()

def test_get_user_by_name():
    response = client.get("/users/Ross Geller")  
    assert response.status_code in [200, 404]  

def test_create_user():
    new_user = {
        "ID": "316082791",  
        "PhoneNumber": "0544340611",
        "Name": "Nadav Erez Elgrabli",  
        "Address": "Tel Aviv"
    }
    response = client.post("/users", json=new_user)
    assert response.status_code in [200, 400] 
