# Это файл конфигурации приложения, здесь может храниться путь к бд, ключ шифрования, что-то еще.
# Чтобы добавить новую настройку, допишите ее в класс.
from pathlib import Path


# Пример

class Config(object):
    DEBUG = True
    SECRET_HERE = '249y823r9v8238r9u'
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{Path(__file__).parent / 'instance' / 'movies.db'}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
