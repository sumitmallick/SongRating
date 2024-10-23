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
    db.create_all()
    load_data_to_db('songs.json')

song_repo = SongRepository()

song_service = SongService(song_repo)

create_song_routes(app, song_service)

if __name__ == '__main__':
    app.run(debug=True)
