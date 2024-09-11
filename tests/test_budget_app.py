import pytest
from app import app
import subprocess
import os

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
        
def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome' in response.data

def test_template_inheritance(client):
    # Test that base.html is being used (assume base.html contains the word 'Footer')
    response = client.get('/')
    assert b'footer' in response.data  # Check if footer text is present

def test_static_css(client):
    # Test that a CSS file is available and linked correctly
    response = client.get('/')
    assert b'<link' in response.data  # Check if a link tag is present
    assert b'.css' in response.data  # Check if a CSS file is linked
    
# def test_git_commits():
#     # Check that at least one commit exists in the Git repository
#     result = subprocess.run(['git', 'rev-list', '--count', 'HEAD'], capture_output=True, text=True)
#     commit_count = int(result.stdout.strip())
#     assert commit_count > 0, "No Git commits found"

def test_git_ignore():
    # Ensure a .gitignore file exists to handle unwanted files
    assert os.path.exists('.gitignore'), ".gitignore file not found"
