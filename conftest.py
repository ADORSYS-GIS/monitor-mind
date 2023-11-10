import pytest
from app import app

@pytest.fixture(scope='session')
def client():
    """Create and configure a test client using the Flask app."""
    with app.test_client() as client:
        yield client