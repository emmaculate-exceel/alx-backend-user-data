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
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=False)
    reset_token = Column(String(250), nullable=False)

    """ def __repr__(self):
         #string representation of object
        
        return (
            "< User(id='%s', email='%s', "
            "hashed_password='%s', "
            "session_id='%s', "
            "reset_token='%s') > " % (
                self.id, self.email,
                self.hashed_password,
                self.session_id,
                self.reset_token
            )
        )
        """
