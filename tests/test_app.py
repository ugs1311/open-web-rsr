import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health_check(client):
    """בדיקת נקודת קצה של בדיקת בריאות"""
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json['status'] == 'healthy'

def test_ollama_connection(client):
    """בדיקת חיבור ל-Ollama"""
    response = client.get('/api/ollama/status')
    assert response.status_code == 200
    assert response.json['connected'] == True

def test_webui_status(client):
    """בדיקת סטטוס ממשק המשתמש"""
    response = client.get('/api/webui/status')
    assert response.status_code == 200
    assert response.json['running'] == True

def test_error_handling(client):
    """בדיקת טיפול בשגיאות"""
    response = client.get('/nonexistent')
    assert response.status_code == 404 