from sqlalchemy import Boolean, Column, Integer, String

from db import Model


class Users(Model):

    __tablename__ = 'Users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)
    age = Column(Integer)


class ItemType(Model):

    __tablename__ = 'item_type'

    item_id = Column(Integer, primary_key=True)
    item_type = Column(String)