from .base import *

SECRET_KEY = env('SECRET_KEY', default='Change secret key.')
DEBUG = env.bool('DEBUG', default=True)

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

