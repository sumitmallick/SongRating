# test_apis.py
import pytest
from app import app
from models.song import db
from flask import json

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client

def test_get_songs(client):
    # Test retrieving songs with pagination
    response = client.get('/api/songs?page=1&per_page=10')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert "data" in data

def test_get_song_by_title(client):
    # Test searching for a song by title
    response = client.get('/api/songs/3AM')
    assert response.status_code == 200 or response.status_code == 404
    data = json.loads(response.data)
    if response.status_code == 200:
        assert "data" in data

def test_rate_song(client):
    # Test rating a song
    response = client.post('/api/songs/093PI3mdUvOSlvMYDwnV1e/rate', json={"rating": 8})
    assert response.status_code == 200 or response.status_code == 404
    data = json.loads(response.data)
    if response.status_code == 200:
        assert "data" in data
