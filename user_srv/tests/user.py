import grpc

import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))  # 把导入路径添加到系统路径上，才能找到同层级下不同文件夹下的proto
sys.path.append(os.path.dirname(SCRIPT_DIR))

from proto.user_pb2 import PageInfo
from proto.user_pb2_grpc import UserStub

class UserTest:
    def __init__(self):
        channel = grpc.insecure_channel("127.0.0.1:3001")
        self.stub = UserStub(channel)

    def user_list(self):
        rsp = self.stub.GetUserList(PageInfo(pn=2))
        print(rsp.total)
        print(rsp.data)
        for user in rsp.data:
            print(user.id, user.mobile)

if __name__ == "__main__":
    user = UserTest()
    user.user_list()