
import pytest
from app import app

@pytest.fixture
def client():
    """Create a test client using Flask's test_client() method."""
    with app.test_client() as client:
        yield client

def test_homepage(client):
    """Test the homepage route."""
    response = client.get('/')
    assert response.status_code == 200
    #assert 'System Metrics' in response.data

def test_cpu_monitoring(client):
    """Test the CPU monitoring API endpoint."""
    response = client.get('/api/cpu')
    assert response.status_code == 200
    # Add more assertions to validate the response data

def test_memory_monitoring(client):
    """Test the memory monitoring API endpoint."""
    response = client.get('/api/memory')
    assert response.status_code == 200
    # Add more assertions to validate the response data

def test_process_tracking(client):
    """Test the process tracking API endpoint."""
    response = client.get('/api/processes')
    assert response.status_code == 404
    # Add more assertions to validate the response data

# Add more test cases for other features as needed