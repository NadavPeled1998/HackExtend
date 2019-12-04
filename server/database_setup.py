import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Group(Base):
    __tablename__ = 'group'

    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    run = Column(Integer, nullable=False)
    #numbers = Column(Integer, nullable=False)

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
# print("yeeee")

