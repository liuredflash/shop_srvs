import json
import nacos
from loguru import logger

# Both HTTP/HTTPS protocols are supported, if not set protocol prefix default is HTTP, and HTTPS with no ssl check(verify=False)
# "192.168.3.4:8848" or "https://192.168.3.4:443" or "http://192.168.3.4:8848,192.168.3.5:8848" or "https://192.168.3.4:443,https://192.168.3.5:443"
# SERVER_ADDRESSES = "127.0.0.1:8848"
# NAMESPACE = "dcd6ac6f-9778-47eb-9a5d-b943aa71f673"

NACOS = {
    "SERVER_ADDRESSES": "127.0.0.1:8848",
    "NAMESPACE": "dcd6ac6f-9778-47eb-9a5d-b943aa71f673",
    "data_id": "user-srv",
    "group": "DEFAULT_GROUP"
}
# no auth mode
client = nacos.NacosClient(NACOS["SERVER_ADDRESSES"], namespace=NACOS["NAMESPACE"])
# auth mode
#client = nacos.NacosClient(SERVER_ADDRESSES, namespace=NAMESPACE, ak="{ak}", sk="{sk}")

# get config
# data_id = "user-srv"
# group = "DEFAULT_GROUP"
NACOS_CONFIG = json.loads(client.get_config(NACOS["data_id"], NACOS["group"]))
print(NACOS_CONFIG)



# DB_SETTINGS = "mysql+pymysql://root:123456@127.0.0.1:3306/user_srv"

# CONSUL_HOST = "172.24.127.154"
# CONSUL_PORT = "8500"

# #user_srv
# SERVICE_NAME = "user_srv"
# SERVICE_TAGS = ["python", "mxshop", "srv"]

DB_SETTINGS = ""

CONSUL_HOST = ""

CONSUL_PORT = 0


#user_srv
SERVICE_NAME = ""

SERVICE_TAGS = ""
def update_config(nacos_config):
    global DB_SETTINGS
    global CONSUL_HOST
    global CONSUL_PORT
    global SERVICE_NAME
    global SERVICE_TAGS
    DB_SETTINGS = nacos_config["DB_SETTINGS"]

    CONSUL_HOST = nacos_config["CONSUL_HOST"]

    CONSUL_PORT = nacos_config["CONSUL_PORT"]

    #user_srv
    SERVICE_NAME = nacos_config["SERVICE_NAME"]

    SERVICE_TAGS = nacos_config["SERVICE_TAGS"]

update_config(NACOS_CONFIG)

def on_update_config(updated_nacos_cofig):
    logger.info("====nacos配置更新======")
    updated_nacos_cofig = json.loads(updated_nacos_cofig["content"])
    logger.info(updated_nacos_cofig)
    update_config(updated_nacos_cofig)

client.add_config_watcher(NACOS["data_id"], NACOS["group"], on_update_config)

