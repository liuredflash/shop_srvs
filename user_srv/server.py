from http import server
from loguru import logger
import signal
import sys

from concurrent import futures
import grpc

from proto import user_pb2, user_pb2_grpc
from handler.user import UserServicer


def on_exit(signo, frame):
    logger.info(f"进程中断 {signo}")
    sys.exit(0)

def init_server(ip, port):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_pb2_grpc.add_UserServicer_to_server(UserServicer(), server)
    server.add_insecure_port(f'{ip}:{port}')

    # 主进程退出信号监听
    signal.signal(signal.SIGINT, on_exit) # ctrl+c
    signal.signal(signal.SIGTERM, on_exit) # kill 进程号
    server.start()
    logger.info(f"========start_grpc_server  {ip}:{port}==========")
    server.wait_for_termination()

if __name__ == "__main__":
    init_server()
