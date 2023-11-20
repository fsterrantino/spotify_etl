import requests
from flask import request
import base64

token_url = 'https://accounts.spotify.com/api/token'

def get_access_token(client_id, client_secret, redirect_uri):
    authorization_code = request.args.get('code')

    # Base64 encode the client_id and client_secret
    client_credentials = f"{client_id}:{client_secret}"
    encoded_credentials = base64.b64encode(client_credentials.encode('utf-8')).decode('utf-8')

    # Token request
    token_headers = {
        'content-type': 'application/x-www-form-urlencoded',
        'Authorization': f'Basic {encoded_credentials}'
    }
 
    token_data = {
        'grant_type': 'authorization_code',
        'code': authorization_code,
        'redirect_uri': redirect_uri
    }

    token_response = requests.post(token_url, headers=token_headers, data=token_data)

    if token_response.status_code == 200:
        # Extract the access token from the response
        access_token = token_response.json()['access_token']
        # Make a request to the Spotify API using the access token
        return access_token
    else:
        # There was an error with the request
        return f'Error al obetener el access_token - {token_response.status_code}: {token_response.text}'