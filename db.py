import sqlite3

class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def user_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,)).fetchmany(1)
            return bool(len(result))

    def add_user(self, user_id, code):
        with self.connection:
            self.cursor.execute("INSERT INTO users (user_id, code) VALUES (?, ?)", (user_id, code))
        self.connection.commit()

    def get_data_users(self):
        with self.connection:
            return self.cursor.execute("SELECT user_id, code FROM users").fetchall()