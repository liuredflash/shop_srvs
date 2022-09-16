from http import server
from loguru import logger

from concurrent import futures
import grpc

from proto import user_pb2, user_pb2_grpc
from handler.user import UserServicer


def init_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_pb2_grpc.add_UserServicer_to_server(UserServicer(), server)
    server.add_insecure_port('[::]:3001')
    server.start()
    logger.info("========start_grpx_server==========")
    server.wait_for_termination()

if __name__ == "__main__":
    init_server()
