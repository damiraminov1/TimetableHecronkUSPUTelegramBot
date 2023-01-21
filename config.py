import os.path
from pathlib import Path
from dotenv import load_dotenv

basedir = Path(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    TOKEN = os.environ.get('BOT_TOKEN')
    URL = 'https://uspu.ru/education/eios/schedule/?group_name='
    DATABASE_URL = os.environ.get('DATABASE_URL')
