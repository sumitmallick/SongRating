# app.py
from flask import Flask
from flask_migrate import Migrate
from models.song import db
from repository.song_repo import SongRepository
from service.song_service import SongService
from router.song_router import create_song_routes
from config import Config
from load_songs_data import load_data_to_db

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

with app.app_context():
    db.create_all()  # Create database tables
    load_data_to_db('songs.json')  # Load JSON data into the database

# Create instance of SongRepository
song_repo = SongRepository()

# Pass the repository instance to SongService
song_service = SongService(song_repo)

# Pass song_service to create_song_routes
create_song_routes(app, song_service)  # Pass the song_service instance here

if __name__ == '__main__':
    app.run(debug=True)
