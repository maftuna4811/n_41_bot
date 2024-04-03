import psycopg2 as db
from main import config


class Database:
    def __init__(self):
        self.connect = db.connect(
            database=config.DB_NAME,
            password=config.DB_PASSWORD,
            user=config.DB_USER,
            host=config.DB_HOST,
           )

        self.cursor = self.connect.cursor()

    def create_tables(self):
        user_table = """
            CREATE TABLE IF NOT EXISTS users(
                id SERIAL PRIMARY KEY,
                full_name VARCHAR(30),
                phone_number VARCHAR(13),
                located VARCHAR(30))
                """
        photos_table = """
            CREATE TABLE IF NOT EXISTS photos(
                id SERIAL PRIMARY KEY,
                user_id INT REFERENCES users(id),
                status BOOLEAN DEFAULT false)
                """
        likes_table = """
            CREATE TABLE IF NOT EXISTS likes(
                id SERIAL PRIMARY KEY,
                user_id INT REFERENCES users(id),
                photo_id INT REFERENCES photos(id)
                is_like BOOLEAN DEFAULT false )
                """

        self.cursor.execute(user_table)
        self.cursor.execute(photos_table)
        self.cursor.execute(likes_table)

        self.connect.commit()


