import os


class Config:
    MYSQL_HOST = os.getenv("DB_HOST")
    MYSQL_USER = os.getenv("MYSQL_USER")
    MYSQL_PASSWORD = os.getenv(
        "MYSQL_PASSWORD",
    )
    MYSQL_DB = os.getenv("MYSQL_DB")
    DEBUG = os.getenv("FLASK_DEBUG")


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False
