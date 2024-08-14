#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative_base import declarative_base
from sqlalchemy.orm import sessionmaker
from slqalchemy.orm.session import session

from user import Base


class DB:
    """DB class
    """
    def __init__(self) -> None:
        """initializing a DB instance
        """
        self.engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self.__engine)
        Base.metadata.create_all(self.__engine)
        self.__session = None

    @property
    def __session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBsession = sessionmaker(bind=self.__engine)
            self.__session = DBsession()
        return self.__session
