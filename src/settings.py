from decouple import config

USER_ID = config('USER_ID')
CLIENT_ID = config('CLIENT_ID')
CLIENT_SECRET = config('CLIENT_SECRET')
REDIRECT_URI = config('REDIRECT_URI')
AUTH_URL = "https://accounts.spotify.com/api/token"
DATABASE_LOCATION = "sqlite:///my_played_tracks.sqlite"