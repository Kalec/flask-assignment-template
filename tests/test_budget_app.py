###  Examine the contents of this file if you want to write your own tests, but
###  Do not edit or otherwise change this!!
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

def test_add_transaction_page(client):
    # Test that the add transaction page loads and contains the transaction form
    response = client.get('/add_transaction')
    assert response.status_code == 200
    assert b'Add Transaction' in response.data  # Check if the page title is present
    assert b'<form' in response.data  # Check if a form is present

def test_form_validation(client):
    # Test that form fields have client-side validation (e.g., 'required' attribute)
    response = client.get('/add_transaction')
    assert b'required' in response.data  # Check if 'required' attribute is used

def test_edit_transaction_page(client):
    # Test that the edit transaction page loads (mock id)
    response = client.get('/edit_transaction/1')
    assert response.status_code == 200
    assert b'Edit Transaction' in response.data  # Check if the page title is present
    assert b'<form' in response.data  # Check if a form is present

def test_manage_categories_page(client):
    # Test that the manage categories page loads and contains the category form
    response = client.get('/categories')
    assert response.status_code == 200
    assert b'Manage Categories' in response.data  # Check if the page title is present
    assert b'<form' in response.data  # Check if a form is present

def test_reports_page(client):
    # Test that the reports page loads correctly
    response = client.get('/reports')
    assert response.status_code == 200
    assert b'Reports' in response.data  # Check if the page title is present

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
