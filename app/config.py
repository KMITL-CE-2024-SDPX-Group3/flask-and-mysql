import os


class Config:
    MYSQL_HOST = os.getenv("DB_HOST")
    MYSQL_USER = os.getenv("MYSQL_USER")
    MYSQL_PASSWORD = os.getenv(
        "MYSQL_PASSWORD",
    )
    MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")
    DEBUG = os.getenv("FLASK_DEBUG")


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False
