import datetime
import time
import requests
import urllib.parse

api_url = 'https://api.spotify.com/v1/me/player/recently-played'

def yesterday_unix():
    today = datetime.datetime.now()
    yesterday = today - datetime.timedelta(days=1)
    yesterday_unix = int(yesterday.timestamp())*1000
    return yesterday_unix


def date_after_to_unixtime(day, month, year):
    date_time = datetime.datetime(year, month, day, 00, 00)
    unix_time = int(date_time.timestamp())*1000
    return unix_time


def songs_request(access_token):

    api_headers = {
        'Authorization': 'Bearer ' +  access_token
    }

    api_data = {
        'after': yesterday_unix(),
        # 'after': date_after_to_unixtime(15, 11, 2023),
        'limit': 20
    }

    # Users data request
    api_url_with_payload = api_url + '?' + urllib.parse.urlencode(api_data)
    api_response = requests.get(api_url_with_payload, headers=api_headers)

    if api_response.status_code == 200:
        print('Consulta realizada Ok.')
        json_response = api_response.json()
        return json_response
    else:
        return f"Error en la Api request - {api_response.status_code}: {api_response.text}"