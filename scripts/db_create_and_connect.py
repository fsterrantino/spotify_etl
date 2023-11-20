import sqlalchemy
import sqlite3

def create_database_and_load_data(df):
    engine = sqlalchemy.create_engine('sqlite:///:memory:')
    conn = sqlite3.connect('my_played_tracks.sqlite')
    cursor = conn.cursor()

    sql_query = """
    CREATE TABLE IF NOT EXISTS my_played_tracks(
        song_name VARCHAR(200),
        artist_name VARCHAR(200),
        played_at VARCHAR(200),
        duration VARCHAR(8),
        CONSTRAINT primary_key_constraint PRIMARY KEY (played_at)
    )
    """
    cursor.execute(sql_query)
    print('Opened database successfully')

    try:
        df.to_sql('my_played_tracks', con=conn, index=False, if_exists='append', method=None)
        print('Datos cargados Ok.')
    except sqlite3.IntegrityError as e:
        print('Data not loaded, error:', e)

    conn.close()
    print('Database closed.')