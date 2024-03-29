import time
from datetime import date
import grpc
from loguru import logger
from model.models import User
from passlib.hash import pbkdf2_sha256
from db import Session
from google.protobuf import empty_pb2

from proto import user_pb2, user_pb2_grpc

class UserServicer(user_pb2_grpc.UserServicer):

    def convert_user_to_userinforesponse(self, user):
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
        return user_info_response


    def GetUserList(self, request: user_pb2.PageInfo, context):
        logger.info("[python 用户列表]")
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
            rsp.data.append(self.convert_user_to_userinforesponse(user))
        return rsp

    @logger.catch  # 抛出异常时，能打印日志
    def GetUserById(self, request, context):
        logger.info(f"===GetUserById===request.id {request.id}===")
        users = Session().query(User).filter(User.id==request.id)
        user_list = users.all()
        if not user_list:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("用户不存在")
            return user_pb2.UserInfoResponse()
        return self.convert_user_to_userinforesponse(user_list[0])

    @logger.catch
    def GetUserByMobile(self, request, context):
        logger.info(f"===GetUserByMobile===request.mobile {request.mobile}===")
        users = Session().query(User).filter(User.mobile==request.mobile)
        user_list = users.all()
        if not user_list:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("用户不存在")
            return user_pb2.UserInfoResponse()
        return self.convert_user_to_userinforesponse(user_list[0])
    
    @logger.catch
    def CreateUser(self, request, context):
        logger.info(f"=================CreateUser======{request.Mobile}========")
        exist_user = Session().query(User).filter(User.mobile == request.Mobile).count()
        if exist_user:
            context.set_code(grpc.StatusCode.ALREADY_EXISTS)
            context.set_details("用户已存在")
            return user_pb2.UserInfoResponse()
        user = User()
        user.nick_name = request.nickName
        user.mobile = request.Mobile
        user.password = request.passWord
        s = Session()
        s.add(user)
        s.commit()
        return self.convert_user_to_userinforesponse(user)
    
    @logger.catch
    def UpdateUser(self, request, context):
        logger.info(f"===UpdateUser===request.id {request.id}===")
        users = Session().query(User).filter(User.id==request.id)
        user_list = users.all()
        if not user_list:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("用户不存在")
            return user_pb2.UserInfoResponse()
        user = user_list[0]
        user.nick_name = request.nickName
        user.gender = request.gengder
        user.birthday = date.fromtimestamp(request.birthDay)
        s = Session()
        s.add(user)
        s.commit()
        return empty_pb2.Empty()

    @logger.catch
    def CheckPassWord(self, request, context):
        return user_pb2.CheckResponse(success=pbkdf2_sha256.verify(request.password, request.encryptedPassword))
