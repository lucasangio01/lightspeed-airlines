import sqlite3
from dotenv import load_dotenv
import os


class DatabaseConnection:
    def __init__(self, table_name):
        load_dotenv()
        db_name = os.environ.get("DB_NAME")
        self.connection = sqlite3.connect(db_name)
        self.cur = self.connection.cursor()
        self.table_name = table_name

    def create_table(self):
        try:
            self.cur.execute(f"CREATE TABLE IF NOT EXISTS {self.table_name}(section, text)")
            print(f"Table '{self.table_name}' created or already existing")
        except Exception as e:
            print(f"Error creating table ({e})")

    def add_record(self):
        try:
            self.cur.execute(f"INSERT INTO {self.table_name} VALUES ('WhoWeAre', 'We are a transportation company, providing services all around the universe')," \
            "('History', 'We were born a long time ago...')")
            print(f"Record(s) added to table {self.table_name}")
            self.connection.commit()
        except Exception as e:
            print(f"Error adding record(s) to table ({e})")

    def fetch_record(self):
        try:
            res = self.cur.execute(f"SELECT * FROM {self.table_name}")
            print(f"Query result:\n {res.fetchall()}")
        except Exception as e:
            print(f"Error fetching record(s) to table ({e})")


def user_interaction():
    user_intention = input("What do you want to do?\n")
    supported_options = ["CREATE_TABLE", "ADD_RECORD", "FETCH_RECORD"]
    chosen_table = input("Which table do you want to work on?\n")
    db = DatabaseConnection(table_name = chosen_table)
    if user_intention not in supported_options:
        raise KeyError
    if user_intention == supported_options[0]:
        db.create_table()
    if user_intention == supported_options[1]:
        db.add_record()
    if user_intention == supported_options[2]:
        db.fetch_record()


user_interaction()