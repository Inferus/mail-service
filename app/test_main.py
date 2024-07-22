from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_send_email_failure():
    response = client.post("/emails", json={"to_email": "invalid-email", "subject": "Test", "body": "Test"})
    assert response.status_code == 422
