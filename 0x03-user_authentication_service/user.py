#!/usr/bin/env python3
""" creating an SQLAlchemy model """
import sqlalchemy
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class User(Base):
    """
    creating a user model
    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    session_id = Column(String, nullable=False)
    reset_token = Column(String, nullable=False)

    def __repr__(self):
        return f"<User(email='{self.email}', hashed_password='{self.hashed_password}', session_id='{self.session_id}', reset_token='{self.reset_token}')>"
