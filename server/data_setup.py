import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


Base = declarative_base()
optsion = ['True', 'False']
class User(Base):
    __tablename__ = 'user'
    username = Column(String(25), primary_key=True)
    password = Column(String(100), nullable=False)
    email = Column(String(250), primary_key=True)
    id = Column(Integer(), nullable=False)
    login = Column(String(7), default='True', nullable=False)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'username': self.username,
            'password': self.password,
            'id': self.id,
            'email': self.email,
            'login': self.login
        }


class Group(Base):
    __tablename__ = 'group'

    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    run = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)


    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'title': self.title,
            'id': self.id,
            'run': self.run
        }


class Member(Base):
    __tablename__ = 'member_item'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    fl = Column(Integer, nullable=False)
    index = Column(Integer, nullable=False)
    group_id = Column(Integer, ForeignKey('group.id'))
    group = relationship(Group)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
            'fl': self.fl,
            'index': self.index
        }


engine = create_engine('sqlite:///data.db')
Base.metadata.create_all(engine)