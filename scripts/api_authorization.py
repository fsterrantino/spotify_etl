import urllib.parse

# Authorization request
def get_authorization_url(client_id, redirect_uri):

    scope = 'user-read-recently-played'  # Add any additional scopes as needed
    base_url = 'https://accounts.spotify.com/authorize'
    params = {
        'client_id': client_id,
        'response_type': 'code',
        'redirect_uri': redirect_uri,
        'scope': scope,
    }

    authorization_url = f"{base_url}?{urllib.parse.urlencode(params)}"
    return authorization_url