from mysql.connector.connection_cext import CMySQLConnection
from mysql.connector import Error
from .database import get_database_connection, set_first_database_connection


def create_database(connection: CMySQLConnection, database_name: str) -> None:
    try:
        cursor = connection.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
        cursor.execute(f"USE {database_name}")
        print(f"Database '{database_name}' is ready.")
    except Error as e:
        print(f"Error creating database: {e}")
    finally:
        cursor.close()


def create_tables(connection: CMySQLConnection) -> None:
    try:
        cursor = connection.cursor()
        user_table_query = """
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            age INT NOT NULL
        )
        """
        cursor.execute(user_table_query)
        print("Tables created successfully.")
    except Error as e:
        print(f"Error creating tables: {e}")
    finally:
        cursor.close()


def insert_initial_data(connection: CMySQLConnection) -> None:
    try:
        cursor = connection.cursor()
        initial_users = [("Alice", 25), ("Bob", 30)]
        query = "INSERT INTO users (name, age) VALUES (%s, %s)"
        cursor.executemany(query, initial_users)
        connection.commit()
        print("Initial data inserted.")
    except Error as e:
        print(f"Error inserting initial data: {e}")


def initialize_database() -> None:
    from flask import current_app

    connection: CMySQLConnection | None = None
    try:
        print("INIT database")
        print("Checking database")

        connection = get_database_connection()
        if connection is not None:
            print("Create new database")
            create_database(connection, current_app.config["MYSQL_DATABASE"])
            create_tables(connection)
            insert_initial_data(connection)
    finally:
        if connection and connection.is_connected():
            connection.close()
            set_first_database_connection()
            print("MySQL connection closed.")
