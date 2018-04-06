import os


VERSION = '0.11.0'

BASE_DIR_NAME = 'zdict'
BASE_DIR = os.path.join(os.path.expanduser('~/.cache'), BASE_DIR_NAME)

DB_NAME = 'zdict.db'
DB_FILE = os.path.join(BASE_DIR, DB_NAME)
