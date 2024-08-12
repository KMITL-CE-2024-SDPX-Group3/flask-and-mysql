import mysql.connector
from mysql.connector import Error
from flask import current_app

is_initialize_database = False


def get_database_config() -> dict[str, any]:
    config = {
        "user": current_app.config["MYSQL_USER"],
        "password": current_app.config["MYSQL_PASSWORD"],
        "host": current_app.config["MYSQL_HOST"],
    }
    if is_initialize_database:
        config["database"] = current_app.config["MYSQL_DB"]
    return config


def set_first_database_connection():
    global is_initialize_database
    is_initialize_database = True


def get_database_connection():
    try:
        config = get_database_config()
        print("CONFIG:", config)
        connection = mysql.connector.connect(**config)

        print("create connection")
        if connection.is_connected():
            print("Connected to MySQL database")
            return connection

    except mysql.connector.InterfaceError as e:
        print(f"Interface Error: Could not connect to MySQL interface - {e}")
        return None

    except mysql.connector.ProgrammingError as e:
        print(f"Programming Error: Configuration or query problem - {e}")
        return None

    except mysql.connector.DatabaseError as e:
        print(f"Database Error: MySQL database problem - {e}")
        return None

    except mysql.connector.DataError as e:
        print(f"Data Error: Data related error - {e}")
        return None

    except mysql.connector.IntegrityError as e:
        print(f"Integrity Error: Data integrity issue - {e}")
        return None

    except mysql.connector.OperationalError as e:
        print(f"Operational Error: Operational issue - {e}")
        return None

    except Error as e:
        print(f"Error connecting to MySQL - db_connect: {e}")
        return None
