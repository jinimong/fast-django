from .base import *

ALLOWED_HOSTS = [
    'localhost', 
    '127.0.0.1',
]

SECRET_KEY = env('SECRET_KEY')
DEBUG = env.bool('DEBUG', default=False)

CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = [
]

