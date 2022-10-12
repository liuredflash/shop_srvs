from pymysql import Date
import datetime

import sqlalchemy

from db import Base
from sqlalchemy import Column
from sqlalchemy import DateTime, Boolean, String, Integer
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref

# 物理删除和逻辑删除的区别，优劣势
# 物理删除重写delete，
# 如何save的时候只更新update_time
# sqlalchemy 可以使用event_listen，after_update,after_insert,after_delete, 或者重写update方法
# from sqlalchemy import event
# event.listen(Session, "before_commit", my_before_commit)
# sqlalchemy 的hook after_attach(), after_begin(), after_bulk_delete(), after_bulk_update(), 
# after_commit(), after_flush(), after_flush_postexec(), after_rollback(), after_soft_rollback(), 
# after_transaction_create(), after_transaction_end(), before_attach(), before_commit(), before_flush(), 
# deleted_to_detached(), deleted_to_persistent(), detached_to_persistent(), do_orm_execute(), loaded_as_persistent(), 
# pending_to_persistent(), pending_to_transient(), persistent_to_deleted(), persistent_to_detached(), persistent_to_transient(), transient_to_pending()


# 外键能保持数据一致性，但会影响性能，因此在分布式微服务不使用外键
# 联合主键
class BaseModel(Base):
    id = Column(Integer, primary_key=True, index=True)
    add_time = Column(DateTime, default=datetime.now)
    update_time = Column(DateTime, default=datetime.now)
    is_deleted = Column(Boolean, default=False)


class Category(BaseModel):
    __tablename__ = "category"
    name = Column(String(20), nullable=True)
    level = Column(Integer, default=1)
    is_tab = Column(Boolean, default=False)
    parent_category = Column(Integer, ForeignKey("category.id"), default=id)
    children_category = relationship("Category", backref=backref("parent_category", remote_side=[id]))

