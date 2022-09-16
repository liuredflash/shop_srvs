import time
from model.models import User
from db import Session

from proto import user_pb2, user_pb2_grpc

class UserServicer(user_pb2_grpc.UserServicer):

    def GetUserList(self, request: user_pb2.PageInfo, context):
        rsp = user_pb2.UserListResponse()
        users = Session().query(User)
        rsp.total = users.count()

        start = 0
        page = 1
        per_page_nums = 10
        if request.pSize:
            per_page_nums = request.pSize
        if request.pn:
            start = per_page_nums * (request.pn-1)
        users = users.limit(per_page_nums).offset(start)
        for user in users:
            user_info_response = user_pb2.UserInfoResponse()
            user_info_response.id = user.id
            user_info_response.passWord = user.password
            user_info_response.mobile  = user.mobile
            if user.role:
                user_info_response.role = user.role
            if user.nick_name:
                user_info_response.nickName = user.nick_name
            if user.gender:
                user_info_response.gender = user.gender
            if user.birthday:
                user_info_response.birthDay = int(time.mktime(user.birthday.timetuple()))
            rsp.data.append(user_info_response)
        return rsp