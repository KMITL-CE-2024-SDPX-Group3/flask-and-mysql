from typing import Optional
from ..models.user import User
from mysql.connector.connection_cext import CMySQLConnection
from mysql.connector import Error


class UserDAO:
    def __init__(self, connection: CMySQLConnection):
        self.connection = connection

    def get_user_by_id(self, user_id: int) -> Optional[User]:
        if self.connection is None:
            raise ValueError("Database connection is not established.")

        cursor = None

        try:
            print(f"[GET]: user_id:{user_id}")
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
            row = cursor.fetchone()
            if row:
                return User(id=row["id"], name=row["name"], age=row["age"])
            return None
        except Error as e:
            print(f"Error reading data from MySQL table: {e}")
            return None
        finally:
            cursor.close()

    def create_user(self, user: User):
        if self.connection is None:
            raise ValueError("Database connection is not established.")
        cursor = None
        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO users (name, age) VALUES (%s, %s)"
            cursor.execute(query, (user.name, user.age))
            self.connection.commit()
            return cursor.lastrowid
        except Error as e:
            print(f"Error inserting data into MySQL table: {e}")
            self.connection.rollback()
            return None
        finally:
            if cursor:
                cursor.close()
