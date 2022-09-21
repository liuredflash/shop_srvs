from loguru import logger
import signal
import sys

from concurrent import futures

from proto import user_pb2, user_pb2_grpc
from handler.user import UserServicer
from common.register.consul_register import ConsulRegister
from common.grpc_health.v1 import health_pb2, health_pb2_grpc
from common.grpc_health.v1 import health
from settings import settings


def on_exit(signo, frame):
    logger.info(f"进程中断 {signo}")
    sys.exit(0)

def init_server(ip, port):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_pb2_grpc.add_UserServicer_to_server(UserServicer(), server)
    # 注册健康检查
    health_pb2_grpc.add_HealthServicer_to_server(health.HealthServicer(), server)

    server.add_insecure_port(f'{ip}:{port}')

    # 主进程退出信号监听
    signal.signal(signal.SIGINT, on_exit) # ctrl+c
    signal.signal(signal.SIGTERM, on_exit) # kill 进程号
    server.start()
    logger.info(f"========start_grpc_server  {ip}:{port}==========")
    logger.info("====注册服务开始")
    register = ConsulRegister(settings.CONSUL_HOST, settings.CONSUL_PORT)
    if not register.register(name=settings.SERVICE_NAME, id=settings.SERVICE_NAME,
             service_address=ip, service_port=port, tags=settings.SERVICE_TAGS, check=None):
             logger.error("服务注册失败")
             sys.exit(0)
    else:
        logger.info("服务注册成功")

    server.wait_for_termination()

if __name__ == "__main__":
    init_server()
