# Spotify API
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# ETL
from src.extract import extract
from src.transform import validate_data
from src.load import Database

# CONSTANTS
from src.settings import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI

auth_manager = SpotifyOAuth(
        client_id=CLIENT_ID, 
        client_secret=CLIENT_SECRET, 
        redirect_uri=REDIRECT_URI, 
        scope='user-read-recently-played'
    )

# Crea un objeto de la API de Spotify con el objeto de autenticación
spotify = spotipy.Spotify(auth_manager=auth_manager)

def run_etl():
    recently_played = spotify.current_user_recently_played()
    song_df = extract(recently_played)

    if validate_data(song_df):
        print("Data valid, proceed to Load stage")
        database = Database(song_df)
        database.init_db()
        database.load()