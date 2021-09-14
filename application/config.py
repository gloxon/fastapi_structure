import json
from configparser import ConfigParser
from pathlib import Path

basedir = Path(__file__).parent.parent
config = ConfigParser()
config.read(Path(basedir, "config.ini"))

basedir = Path(__file__).parent
DEBUG = json.loads(str(config.get('base', 'DEBUG')).lower())


class Config:

    SECRET_KEY = config.get('base', 'SECRET_KEY')
    DEBUG = DEBUG 

    # Database 
    DB_NAME = config.get('database', 'DB_NAME')
    DB_USERNAME = config.get('database', 'DB_USERNAME')
    DB_PASSWORD = config.get('database', 'DB_PASSWORD')
    DB_HOST = config.get('database', 'DB_HOST')
    DB_PORT = config.get('database', 'DB_PORT')
    SQLALCHEMY_DATABASE_URI = f'mysql+mysqldb://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'




settings = Config()

