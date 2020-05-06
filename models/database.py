import sqlite3
from sqlite3 import Error
import os



FILE = "playlists.db" 
PLAYLIST_TABLE = "Playlists"
VIBES = ["None", "HAPPY", "CALM", "SAD", "ENERGETIC"]


class DataBase:
    def __init__(self):
        self.playlists = None

        self.conn = None
        try:
            self.conn = sqlite3.connect(FILE)
        except Error as e:
            print(e)

        self.cursor = self.conn.cursor()
        self._create_table()

    def close(self):
        self.conn.close()

    def _create_table(self):
        query = f"""CREATE TABLE IF NOT EXISTS {PLAYLIST_TABLE}
                    (url_music TEXT, vibe TEXT, id INTEGER PRIMARY KEY AUTOINCREMENT)"""
        self.cursor.execute(query)
        self.conn.commit()

    def get_playlists_by_vibe(self, vibe):
        query = f"SELECT * FROM {PLAYLIST_TABLE} WHERE vibe=?"
        self.cursor.execute(query, (vibe,))

        result = self.cursor.fetchall()

        results = []
        for r in result:
            url_music, vibe, _id = r
            results.append(url_music)

        return results
