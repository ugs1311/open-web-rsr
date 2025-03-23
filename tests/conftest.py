import pytest
import os
import sys

# הוספת תיקיית הפרויקט ל-PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

@pytest.fixture(autouse=True)
def setup_test_env():
    """הגדרת סביבת בדיקה"""
    os.environ['FLASK_ENV'] = 'testing'
    os.environ['TESTING'] = 'true'
    yield
    # ניקוי אחרי הבדיקות
    if os.path.exists('test.db'):
        os.remove('test.db')

@pytest.fixture
def mock_ollama():
    """Mock של שירות Ollama"""
    class MockOllama:
        def __init__(self):
            self.connected = True
            self.model = 'llama.bin'
            self.port = 11010

        def is_connected(self):
            return self.connected

        def get_model(self):
            return self.model

        def get_port(self):
            return self.port

    return MockOllama()

@pytest.fixture
def mock_webui():
    """Mock של ממשק המשתמש"""
    class MockWebUI:
        def __init__(self):
            self.running = True
            self.port = 5000

        def is_running(self):
            return self.running

        def get_port(self):
            return self.port

    return MockWebUI() 