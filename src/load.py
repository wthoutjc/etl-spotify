import pandas as pd

# DB
import sqlite3
import sqlalchemy

# Settings
from src.settings import DATABASE_LOCATION

class Database:
    def __init__(self, song_df:'pd.DataFrame'):
        self.engine = sqlalchemy.create_engine(DATABASE_LOCATION)
        self.conn = sqlite3.connect('my_played_tracks.sqlite')
        self.cursor = self.conn.cursor()

        self.song_df = song_df

    def init_db(self):
        sql_query = """
        CREATE TABLE IF NOT EXISTS my_played_tracks(
            song_name VARCHAR(200),
            artist_name VARCHAR(200),
            played_at VARCHAR(200),
            timestamp VARCHAR(200),
            CONSTRAINT primary_key_constraint PRIMARY KEY (played_at)
        )
        """
        self.cursor.execute(sql_query)
    
    def load(self):
        try:
            self.song_df.to_sql("my_played_tracks", self.engine, index=False, if_exists='append')
        except:
            print("Data already exists in the database")
        finally:
            self.conn.close()
            print("Close database connection")