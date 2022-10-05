import argparse
from model.models import *
from loguru import logger
from db import init_db
from server import init_server
from settings import settings



def init_log():
    logger.add("logs/user_srv{time}.log")
def main():
    # 命令行启动可传参
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--ip",
        nargs="?",
        type=str,
        default="192.168.68.106",
        help="binding ip"
    )
    parser.add_argument(
        "--port",
        nargs="?",
        type=str,
        default="0",
        help="binding port"
    )
    args = parser.parse_args()
    init_log()
    init_db(settings.DB_SETTINGS)
    init_server(args.ip, args.port)
    # settings.client.add_config_watcher(settings.NACOS["data_id"], settings.NACOS["group"], settings.on_update_config) 
    # 不能放在这里，因为程序在 init_server中已经停下监听


def config_updated():
    init_db(settings.DB_SETTINGS)

if __name__ == "__main__":
    main()