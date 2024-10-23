# router/song_router.py
from flask import Blueprint, jsonify, request, abort
from service.song_service import SongService

song_blueprint = Blueprint('song_blueprint', __name__)

def create_song_routes(app, song_service: SongService):  # Accept song_service as an argument
    @app.route('/api/songs', methods=['GET'])
    def get_songs():
        try:
            page = int(request.args.get('page', 1))
            per_page = int(request.args.get('per_page', 10))
            all_songs, count = song_service.get_paginated_songs(page, per_page)
            all_songs = [song.to_dict() for song in all_songs]  # Convert db objects to dict
            if all_songs:
                return jsonify({
                        "status": 200,
                        "status_message": "Successfully retrieved all songs",
                        "total_count": count,
                        "data": all_songs
                    }), 200
        except Exception as e:
            return jsonify({
                    "status": 400,
                    "status_message": str(e)
                }), 400


    @app.route('/api/songs/<string:title>', methods=['GET'])
    def get_song_by_title(title):
        try:
            song = song_service.get_song_by_title(title)
            if not song:
                return jsonify({
                        "status": 404,
                        "status_message": "No song present by song_id: " + song_id
                    }), 404

            return jsonify({
                        "status": 200,
                        "status_message": "Successfully retrieved song details by title: " + title,
                        "data": song.to_dict()  # Convert Song object to dict
                    }), 200
        except Exception as e:
            return jsonify({
                    "status": 400,
                    "status_message": str(e)
                }), 400


    @app.route('/api/songs/<string:song_id>/rate', methods=['POST'])
    def rate_song(song_id):
        rating = request.json.get('rating')
        if not 1 <= rating <= 10:
            return jsonify({
                        "status": 401,
                        "status_message": "Rating must be between 1 and 10"
                    }), 401
        try:
            song = song_service.rate_song(song_id, rating)

            if song:
                return jsonify({
                    "status": 200,
                    "status_message": "Successfully updated rating of the song by song_id: " + song_id,
                    "data": song.to_dict()  # Convert Song object to dict
                }), 200

            else:
                return jsonify({
                    "status": 404,
                    "status_message": "No song present by song_id: " + song_id
                }), 404

        except ValueError as e:
            return jsonify({
                    "status": 400,
                    "status_message": str(e)
                }), 400

