from model.models import *
from loguru import logger
from db import init_db
from server import init_server
from settings import settings



def init_log():
    logger.add("logs/user_srv{time}.log")
def main():
    init_log()
    init_db(settings.DB_SETTINGS)
    init_server()


def config_updated():
    init_db(settings.DB_SETTINGS)

if __name__ == "__main__":
    main()