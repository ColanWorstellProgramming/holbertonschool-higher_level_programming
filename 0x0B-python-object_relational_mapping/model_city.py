#!/usr/bin/python3
"""model city"""
from sqlalchemy import String, Integer, Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class City(Base):
    """city class"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
