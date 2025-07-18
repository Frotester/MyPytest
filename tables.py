from sqlalchemy import Boolean, Column, Integer, String

from db import Model

class Users(Model):

    __tablename__ = 'Users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)
    age = Column(Integer)