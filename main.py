from flask import Flask, redirect
from scripts.client_info import client_id, client_secret
from scripts.api_authorization import get_authorization_url
from scripts.api_get_token import get_access_token
from scripts.api_songs_request import songs_request
from scripts.parse_response import parse_song_data
from scripts.db_create_and_connect import create_database_and_load_data

app = Flask(__name__)

redirect_uri = 'http://127.0.0.1:5000/callback'

@app.route('/')
def index():
    auth_url = get_authorization_url(client_id, redirect_uri)
    return redirect(auth_url)

@app.route('/callback', methods=['GET'])
def callback():
    access_token = get_access_token(client_id, client_secret, redirect_uri)
    songs_dict = songs_request(access_token)
    songs_df = parse_song_data(songs_dict)

    if not songs_df.empty:
        create_database_and_load_data(songs_df)
        return songs_df.to_html()

    return print('No se escucharon canciones este día.')

if __name__ == '__main__':
    app.run(debug=True)