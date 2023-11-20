import pandas as pd
import datetime
from dateutil import parser

def parse_artist(song):
    dict_artists = song['track'].get('artists', None)
    artists = []

    for artist in dict_artists:
        artists.append(artist['name'])

    return artists

def parse_duration(duration_ms):
    if duration_ms == None:
        return None
    
    millis = duration_ms
    millis = int(millis)
    seconds = (millis/1000)%60
    seconds = int(seconds)
    minutes = (millis/(1000*60))%60
    minutes = int(minutes)
    hours = (millis/(1000*60*60))%24
    duration = "%02d:%02d:%02d" % (hours, minutes, seconds)
    return duration

def check_unique_key_values(df):
    if not df['played_at'].is_unique:
        raise Exception('Primary key is violated')
    
def check_null_values(df):
    if df.isnull().values.any():
        raise Exception('Null values found')

def check_songs_are_from_yesterday(df):
    today = datetime.datetime.now()
    yesterday_timestamp = today - datetime.timedelta(days=1)
    yesterday = yesterday_timestamp.date()

    df = df[df['played_at'].str[:10] == yesterday.strftime('%Y-%m-%d')]
    return df

    timestamps = df['played_at'].to_list()
    for timestamp in timestamps:
        if parser.parse(timestamp).date() != yesterday:
            raise Exception('At least un row is not from yesterday.')

def check_df_constraints(df):
    check_unique_key_values(df)
    check_null_values(df)
    df = check_songs_are_from_yesterday(df)
    print('Data is Ok to load.')
    return df

def parse_song_data(song_dict):
    songs_list = []
    
    if song_dict['items']:
        for song in song_dict['items']:     
            song_data = {
                'song_name': song['track'].get('name', None)
                , 'artist_name': parse_artist(song)
                , 'played_at': song.get('played_at', None)
                , 'duration':  parse_duration(song['track'].get('duration_ms', None))
            }
            songs_list.append(song_data)

        songs_df = pd.DataFrame.from_dict(songs_list)
        songs_df['artist_name'] = [','.join(map(str, artist)) for artist in songs_df['artist_name']]

        songs_df = check_df_constraints(songs_df)
        return songs_df
    
    else:
        print('No se escucharon canciones este día')
        return songs_df

