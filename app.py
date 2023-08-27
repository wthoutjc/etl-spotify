# Spotify API
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Extract
from src.extract import extract

# Tools
from decouple import config

# DB
import sqlalchemy
import sqlite3
from sqlalchemy.orm import sessionmaker

# CONSTANTS
DATABASE_LOCATION = "sqlite:///my_played_tracks.sqlite"
USER_ID = "psykobaby"
CLIENT_ID = config('CLIENT_ID')
CLIENT_SECRET = config('CLIENT_SECRET')
AUTH_URL = "https://accounts.spotify.com/api/token"
REDIRECT_URI = "http://localhost:8888/callback/"

auth_manager = SpotifyOAuth(
        client_id=CLIENT_ID, 
        client_secret=CLIENT_SECRET, 
        redirect_uri=REDIRECT_URI, 
        scope='user-read-recently-played'
    )

# Crea un objeto de la API de Spotify con el objeto de autenticación
spotify = spotipy.Spotify(auth_manager=auth_manager)

if __name__ == "__main__":
    # Obtener la información de reproducción reciente del usuario
    recently_played = spotify.current_user_recently_played()
    song_df = extract(recently_played)

    

    