import pandas as pd

def validate_data(df_song:'pd.DataFrame') -> bool:
    if df_song.empty:
        print("No songs downloaded. Finishing execution")
        return False

    # Primary Key Check
    if not pd.Series(df_song['played_at']).is_unique:    
        print("Primary Key check is violated")
        return False
    
    # Check for nulls
    if df_song.isnull().values.any():
        print("Null values found")
        return False
    
    # Check that all timestamps are of yesterday's date
    yesterday = pd.Timestamp.now() - pd.Timedelta(days=1)
    yesterday = yesterday.replace(hour=0, minute=0, second=0, microsecond=0)

    timestamps = df_song["timestamp"].tolist()
    for timestamp in timestamps:
        if pd.Timestamp(timestamp) != yesterday:
            print("At least one of the returned songs does not have a yesterday's timestamp")
            return False
    

