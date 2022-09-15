from model.models import *
from db import init_db
from settings import settings


def main():
    init_db(settings.DB_SETTINGS)


def config_updated():
    init_db(settings.DB_SETTINGS)