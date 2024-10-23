# models/song.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Song(db.Model):
    __tablename__ = 'songs'

    id = db.Column(db.String, primary_key=True)
    title = db.Column(db.String, nullable=False)
    danceability = db.Column(db.Float)
    energy = db.Column(db.Float)
    key = db.Column(db.Integer)
    loudness = db.Column(db.Float)
    mode = db.Column(db.Integer)
    acousticness = db.Column(db.Float)
    instrumentalness = db.Column(db.Float)
    liveness = db.Column(db.Float)
    valence = db.Column(db.Float)
    tempo = db.Column(db.Float)
    duration_ms = db.Column(db.Float)
    time_signature = db.Column(db.Integer)
    num_bars = db.Column(db.Integer)
    num_sections = db.Column(db.Integer)
    num_segments = db.Column(db.Integer)
    rating = db.Column(db.Integer)
    class_type = db.Column(db.Integer)

    def __init__(self, id, title, danceability, energy, key, loudness, mode, acousticness, instrumentalness, liveness, valence, tempo, duration_ms, time_signature, num_bars, num_sections, num_segments, class_type, rating=None):
        self.id = id
        self.title = title
        self.danceability = danceability
        self.energy = energy
        self.key = key
        self.loudness = loudness
        self.mode = mode
        self.acousticness = acousticness
        self.instrumentalness = instrumentalness
        self.liveness = liveness
        self.valence = valence
        self.tempo = tempo
        self.duration_ms = duration_ms
        self.time_signature = time_signature
        self.num_bars = num_bars
        self.num_sections = num_sections
        self.num_segments = num_segments
        self.class_type = class_type
        self.rating = rating

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'danceability': self.danceability,
            'energy': self.energy,
            'key': self.key,
            'loudness': self.loudness,
            'mode': self.mode,
            'acousticness': self.acousticness,
            'instrumentalness': self.instrumentalness,
            'liveness': self.liveness,
            'valence': self.valence,
            'tempo': self.tempo,
            'duration_ms': self.duration_ms,
            'time_signature': self.time_signature,
            'num_bars': self.num_bars,
            'num_sections': self.num_sections,
            'num_segments': self.num_segments,
            'class_type': self.class_type,
            'rating': self.rating
        }
