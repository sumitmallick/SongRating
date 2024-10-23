# Flask Song API

This project provides a REST API to retrieve and manage a dataset of songs. You can retrieve songs, search for a song by title, and rate songs.

## Table of Contents
- [Setup](#setup)
- [Testing](#testing)
- [API Documentation](#api-documentation)
- [Scalability & Improvements](#scalability--improvements)

## Setup

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_directory>

2. Create a virtual env
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt

3. Initialize the database:
   ```bash
   flask db init
   flask db migrate
   flask db upgrade

4. Load the song data from songs.json: The songs.json file contains a dataset of songs, and the data will be loaded into the database when the app starts.

5. Run the app:
   ```bash
   python app.py --debug # in case want to debug

6. To run tests, using pytest:
   ```bash
   pytest test_apis.py

## API Documentation

1. Retrieve Songs with Pagination
      URL: /api/songs
      Method: GET
      Query Params:
      page: Page number (default: 1)
      per_page: Number of songs per page (default: 10)
      Response:
      Status: 200
      Data: List of songs

      {
         "status": 200,
         "status_message": "Successfully retrieved all songs",
         "total_count": 100,
         "data": [
            {
               "id": 1,
               "title": "Song Title",
               "artist": "Artist Name",
               "rating": 4
            }
         ]
      }

   CURL Command:
   ```bash
   curl --location 'http://127.0.0.1:5000/api/songs?page=1&per_page=10'

2. Search Song by Title
      URL: /api/songs/<title>
      Method: GET
      Response:
      Status: 200
      Data: Song details

      {
         "status": 200,
         "status_message": "Successfully retrieved song details",
         "data": {
            "id": 1,
            "title": "Song Title",
            "artist": "Artist Name",
            "rating": 4
         }
      }

      CURL Command:
      ```bash
      curl --location 'http://127.0.0.1:5000/api/songs/3AM'

3. Rate a Song
      URL: /api/songs/<song_id>/rate
      Method: POST
      Body:
      rating: An integer between 1 and 10
      Response:
      Status: 200
      Data: Updated song details

      {
         "status": 200,
         "status_message": "Successfully updated rating",
         "data": {
            "id": 1,
            "title": "Song Title",
            "artist": "Artist Name",
            "rating": 8
         }
      }

      CURL Command:
      ```bash
      curl --location 'http://127.0.0.1:5000/api/songs/093PI3mdUvOSlvMYDwnV1e/rate' \
      --header 'Content-Type: application/json' \
      --data '{
         "rating": 8.7
      }'


## Scalability & Improvements

- **Caching**: Use Redis or Memcached to cache song data, reducing the load on the database.
- **Task Queues**: Use Celery for background processing, like calculating average ratings or batch data imports.
- **Database Optimization**: Add indexing to fields like song title or artist to optimize search queries.
- **Horizontal Scaling**: Containerize the app with Docker and orchestrate using Kubernetes or ECS for better horizontal scalability.
- **Load Balancing**: Set up NGINX for load balancing to handle concurrent users.
- **Rate Limiting**: Use rate-limiting to protect against API abuse.
- **CI/CD**: Set up CI/CD pipelines to automate testing, building, and deployment.
