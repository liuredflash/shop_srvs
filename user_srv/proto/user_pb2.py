# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: user.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nuser.proto\x1a\x1bgoogle/protobuf/empty.proto\"%\n\x08PageInfo\x12\n\n\x02pn\x18\x01 \x01(\r\x12\r\n\x05pSize\x18\x02 \x01(\r\"\x1f\n\rMobileRequest\x12\x0e\n\x06mobile\x18\x01 \x01(\t\"\x17\n\tIdRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"D\n\x0e\x43reateUserInfo\x12\x10\n\x08nickName\x18\x01 \x01(\t\x12\x10\n\x08passWord\x18\x02 \x01(\t\x12\x0e\n\x06Mobile\x18\x03 \x01(\t\"Q\n\x0eUpdateUserInfo\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x10\n\x08nickName\x18\x02 \x01(\t\x12\x0f\n\x07gengder\x18\x03 \x01(\t\x12\x10\n\x08\x62irthDay\x18\x04 \x01(\x04\"\x82\x01\n\x10UserInfoResponse\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x10\n\x08passWord\x18\x02 \x01(\t\x12\x0e\n\x06mobile\x18\x03 \x01(\t\x12\x10\n\x08nickName\x18\x04 \x01(\t\x12\x10\n\x08\x62irthDay\x18\x05 \x01(\t\x12\x0e\n\x06gender\x18\x06 \x01(\t\x12\x0c\n\x04role\x18\x07 \x01(\x05\"B\n\x10UserListResponse\x12\r\n\x05total\x18\x01 \x01(\x05\x12\x1f\n\x04\x64\x61ta\x18\x02 \x03(\x0b\x32\x11.UserInfoResponse2\x80\x02\n\x04User\x12+\n\x0bGetUserList\x12\t.PageInfo\x1a\x11.UserListResponse\x12\x34\n\x0fGetUserByMobile\x12\x0e.MobileRequest\x1a\x11.UserInfoResponse\x12,\n\x0bGetUserById\x12\n.IdRequest\x1a\x11.UserInfoResponse\x12\x30\n\nCreateUser\x12\x0f.CreateUserInfo\x1a\x11.UserInfoResponse\x12\x35\n\nUpdateUser\x12\x0f.UpdateUserInfo\x1a\x16.google.protobuf.EmptyB\tZ\x07.;protob\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'user_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\007.;proto'
  _PAGEINFO._serialized_start=43
  _PAGEINFO._serialized_end=80
  _MOBILEREQUEST._serialized_start=82
  _MOBILEREQUEST._serialized_end=113
  _IDREQUEST._serialized_start=115
  _IDREQUEST._serialized_end=138
  _CREATEUSERINFO._serialized_start=140
  _CREATEUSERINFO._serialized_end=208
  _UPDATEUSERINFO._serialized_start=210
  _UPDATEUSERINFO._serialized_end=291
  _USERINFORESPONSE._serialized_start=294
  _USERINFORESPONSE._serialized_end=424
  _USERLISTRESPONSE._serialized_start=426
  _USERLISTRESPONSE._serialized_end=492
  _USER._serialized_start=495
  _USER._serialized_end=751
# @@protoc_insertion_point(module_scope)
