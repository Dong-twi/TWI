from sqlalchemy import Column, Integer,String,Boolean,Date

from .database import Base

#Define Model
class Todo(Base):
    __tablename__="todos"
    id=Column(Integer,primary_key=True)
    title =Column(String(100),nullable=False)
    description =Column(String,nullable=True)
    completed =Column(Boolean,default=False)
    due_date = Column(Date, nullable=True)
class user(Base):
    __tablename__="user"
    id=Column(Integer,primary_key=True)
    username = Column(String, nullable = False)
    password = Column(String, nullable = False)
    email = Column(String, nullable = True)