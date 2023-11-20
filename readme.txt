Project: 
    Spotify ETL

Objective:
    Code a program that manages to connect to Spotify users info, download songs listened the day before (20 of them), and load them into a DB.

Resources used:
    - Python
    - SpotifyAPI
    - SQLite
    - DBeaver

Use:
    - In order to run the App it's needed to configure a customer id and secret (directory: scripts/client_info.py)
    - The Flask backend needs to be up and running (main.py)
    - Access the localhost where the main.py it's running.
    - Log in to Spotify Api (tracks resources need permission from the user). This gives to the backend a specific URL to obtain the token for the request.
    - The app process the request automatically. It will generate the DB, if it's not created. Request and parse the info. Run a serie of controls. And finally load the information.
    - I use DBeaver to access the SQLite file that's going to be created. (my_played_tracks)