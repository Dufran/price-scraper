from .common import *
DEBUG = True
SECRET_KEY = os.environ.get('SECRET_KEY')
FORCE_SCRIPT_NAME = "/price-scraper/"
STATIC_URL = "/price-scraper/backend/static/"
STATIC_ROOT = "/price-scraper/backend/static"
