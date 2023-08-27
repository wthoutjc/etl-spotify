import pandas as pd

def extract(recently_played):
    song_names = []
    artist_names = []
    played_at_list = []
    timestamps = []

    # Iterar sobre el diccionario de reproducción reciente y obtener los datos relevantes
    for song in recently_played["items"]:
        song_names.append(song["track"]["name"])
        artist_names.append(song["track"]["album"]["artists"][0]["name"])
        played_at_list.append(song["played_at"])
        timestamps.append(song["played_at"][0:10])

    # Crear un diccionario que contenga los datos relevantes
    song_dict = {
        "song_name": song_names,
        "artist_name": artist_names,
        "played_at": played_at_list
    }

    # Crear un dataframe
    song_df = pd.DataFrame(song_dict, columns=["song_name", "artist_name", "played_at"])
    return song_df